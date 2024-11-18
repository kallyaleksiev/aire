import asyncio
from collections import Counter
from typing import Dict, cast

from aire.errors import AIREError

try:
    import openai

    _aclient = openai.AsyncOpenAI()

except openai.OpenAIError as e:
    if "or by setting the OPENAI_API_KEY environment variable" in str(e):
        raise AIREError(
            reason="Right now you can only configure the underlying OpenAI client via environment variales, sorry.",
            underlying_error=e,
        )
    else:
        raise AIREError(reason="Unknown.", underlying_error=e)


def get_pattern(
    pattern_explanation: str,
    best_of: int = 3,
    max_concurrent: int = 3,
) -> str:
    return asyncio.run(async_get_pattern(pattern_explanation, best_of, max_concurrent))


async def async_get_pattern(
    pattern_explanation: str,
    best_of: int = 3,
    max_concurrent: int = 3,
) -> str:
    result_cache: Dict[str, int] = {}
    user_prompt = _get_prompt(pattern_explanation)

    sem = asyncio.Semaphore(max_concurrent)

    tasks = [_async_get_pattern_from_oai(user_prompt, sem) for _ in range(best_of)]
    candidate_patterns = await asyncio.gather(*tasks)

    # majority vote
    pattern_counts = Counter(pattern for pattern in candidate_patterns if pattern is not None)
    if not pattern_counts:
        raise AIREError(
            reason="Model failed to follow instructions at every time.",
        )
    else:
        top_pattern, _ = pattern_counts.most_common(1)[0]
        return top_pattern


def _get_prompt(
    pattern_explanation: str,
) -> str:
    return (
        "Give me a Python r-string for a regex pattern exactly according to "
        f"the following explanation:\n{pattern_explanation}\n"
        "Your output should contain just a single line containing the pattern."
        "Do not include anything else. May the pattern appear exactly as you would "
        "write it in Python source code.\n\nHere is an example:\n\n"
        "*Given Explanation*: number indicating line item followed by a dot, space, "
        "and then the name of the section, such as: 1. Introduction\n"
        '*Ideal Answer*: r"^\\d+\\. [A-Za-z ]+$"'
    )


def _extract_pattern_from_model_response(model_response: str) -> str:
    if model_response.startswith('r"'):
        return model_response[len('r"') : -len('"')]
    elif model_response.startswith('```python\nr"'):
        return model_response[len('```python\nr"') : -len('"\n```')]
    else:
        raise AIREError(
            reason="Model did not follow instructions.",
        )


async def _async_get_pattern_from_oai(
    user_prompt: str,
    sem: asyncio.Semaphore,
) -> str | None:
    _system_prompt = (
        "You are a helpful assistant with vast knowledge of regular expressions. "
        "You always reply concisely and accurately. You follow user instructions "
        "exactly as they are given and you output in exactly the kind of format "
        "the user is asking for."
    )

    messages = [
        {
            "role": "system",
            "content": _system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    try:
        async with sem:

            response = await _aclient.chat.completions.create(
                model="gpt-4o",
                messages=messages,  # type: ignore
            )
            return _extract_pattern_from_model_response(cast(str, response.choices[0].message.content))

    except Exception:
        return None
