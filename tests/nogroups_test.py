import aire

test_cases_with_explanations = [
    (
        "First $ {} Second Something Else",
        "It should match the string consisting of $ followed by space and then two closed curly braces {} anywhere in a larger string",
    ),
    (
        "...''\"",
        "It should match exactly the string ...''\" -- i.e. consisting of 3 dots, two single quotes, and a double quote exactly",
    ),
    (
        "First A, B, C Second Something Else",
        "It should match the string consisting of the letters A, B, C separated by commas in that order, i.e. 'A, B, C' anywhere in a larger string",
    ),
]


def test_one():
    test_case, model_explanation = test_cases_with_explanations[0]

    aire_pattern = aire.compile(model_explanation)

    assert aire_pattern.search(test_case) is not None
    assert aire_pattern.search(test_case).span() == (6, 10)


def test_two():
    test_case, model_explanation = test_cases_with_explanations[1]

    aire_pattern = aire.compile(model_explanation, best_of=3)

    assert aire_pattern.match(test_case) is not None
    assert aire_pattern.match(test_case).span() == (0, len(test_case))


def test_three():
    test_case, model_explanation = test_cases_with_explanations[2]

    aire_pattern = aire.compile(model_explanation)

    assert aire_pattern.search(test_case) is not None
    assert aire_pattern.search(test_case).span() == (6, 13)
