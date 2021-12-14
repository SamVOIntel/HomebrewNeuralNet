import pytest
from assets.movies import MovieScore


@pytest.mark.parametrize(
    "score, lower, upper, expected_result",
    [
        (50, 0, 100, None),             # good and normal
        (50, 51, 100, ValueError),      # lower bound is too high
        (50, 0, -6, ValueError),        # Upper bound is too low
        (101, 0, 100, ValueError),      # value is too high
        (-6, 0, 100, ValueError),       # value is too low
        ("bananas", 0, 100, TypeError), # value is not int
        (0, "bananas", 100, TypeError), # lower is not int
        (0, 0, "bananas", TypeError),   # upper is not int
    ]
)
def test_create_moviescore(score, lower, upper, expected_result):
    try:
        MovieScore(score, lower, upper)
    except expected_result:
        assert True
    except Exception:
        assert False


@pytest.mark.parametrize(
    "new_val, expected_result",
    [
        (25, None),                     # good and normal
        ("bananas", TypeError),         # value is wrong type
        (25.1, TypeError),              # value is wrong type
        (-6, ValueError),               # value is too low
        (105, ValueError),              # value is too high
    ]
)
def test_setting_value(new_val, expected_result):
    test_obj = MovieScore(50)
    try:
        test_obj.value = new_val
    except expected_result:
        assert True
    except Exception:
        assert False


@pytest.mark.parametrize(
    "new_low, new_high, expected_result",
    [
        (25, 100, None),                    # good and normal
        ("bananas", 100, TypeError),        # low_bound is wrong type
        (0, "bananas", TypeError),          # high_bound is wrong type
        (25.1, 100, TypeError),             # low_bound is wrong type
        (25, 100.1, TypeError),             # high_bound is wrong type
        (105, 100, ValueError),             # low_bound is too high
        (0, -6, ValueError),                # high_bound is too low
    ]
)
def test_setting_bounds(new_low, new_high, expected_result):
    test_obj = MovieScore(50)
    try:
        test_obj.lower = new_low
        test_obj.upper = new_high
    except expected_result:
        assert True
    except Exception:
        assert False
