import aire

test_cases_with_explanations = [
    (
        "This movie is so good! Rating: 5, Votes: 14214289 I can't believe I haven't seen it before",
        "Regex with two groups. Strings will be descriptions of movies and at some point you have rating, colon number from 1 to 5 and then Votes, colon and any natural number. Extract them in the two groups. Example is This movie is nice. Rating: 5, Votes: 1456",
    ),
    (
        "TESTING A: {15}, B: {187}, C: {394}. END OF TESTING",
        "Regex with 3 groups. Has to match the string A: {number here}, B: {number here}, C: {number here}. The curly braces will be there. Example is '<smth>...A: {15}, B: {187}, C: {394}...<smth>'",
    ),
]


def test_one():
    test_case, model_explanation = test_cases_with_explanations[0]

    aire_pattern = aire.compile(model_explanation)

    assert aire_pattern.search(test_case) is not None
    assert aire_pattern.search(test_case).groups()[0] == "5"
    assert aire_pattern.search(test_case).groups()[1] == "14214289"


def test_two():
    test_case, model_explanation = test_cases_with_explanations[1]

    aire_pattern = aire.compile(model_explanation)

    assert aire_pattern.search(test_case) is not None
    assert aire_pattern.search(test_case).groups()[0] == "15"
    assert aire_pattern.search(test_case).groups()[1] == "187"
    assert aire_pattern.search(test_case).groups()[2] == "394"
