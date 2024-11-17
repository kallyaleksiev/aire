import re

from aire.utils import get_pattern


def compile(
    pattern_explanation: str,
    best_of: int = 3,
    max_concurrent: int = 3,
    flags: re.RegexFlag = re.RegexFlag.NOFLAG,
) -> re.Pattern:
    """The equivalent of the `re.compile` but where the actual regular expression is discovered
    by an AI model.

    Args:
        pattern_explanation (str): The natural language explanation for the regular expression.
        best_of (int): The number of attempts to the model from which majority vote will be taken. Defaults to 3.
        max_concurrent (int): The maximum number of concurrent requests to the model. Defaults to 3.
        flags (re.RegexFlag, optional): The flags to be used in the regular expression.
        Defaults to re.RegexFlag.NOFLAG.
    """

    pattern = get_pattern(pattern_explanation, best_of=best_of)

    return re.compile(
        pattern,
        flags=flags,
    )
