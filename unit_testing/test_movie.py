import pytest
from assets.movies import Movie


@pytest.mark.parametrize(
    "title, year, rating, director, rottom, imdb, expected_result",
    [
        ("Bananas", 1999, 100, "Sam VO", 66, 78, None),         # good and normal
        (12, 1999, 100, "Sam VO", 66, 78, TypeError),           # title is wrong type
        ("Bananas", 1999.5, 100, "Sam VO", 66, 78, TypeError),  # year is wrong type
        ("Bananas", 1999, 100, lambda x: x, 66, 78, TypeError), # director is wrong type
    ]
)
def test_create_movie(title, year, rating, director, rottom, imdb, expected_result):
    try:
        Movie(title, year, rating, director, rottom, imdb)
    except expected_result:
        assert True
    except Exception:
        assert False


def test_create_private_attrs():
    test_obj = Movie("Bananas", 1999, 100, "Sam VO", 66, 78)
    try:
        test_obj.title = "NOT Bananas"
        assert False
    except AttributeError:
        assert True
    except Exception:
        assert False
    try:
        test_obj.year = "NOT 1999"
    except AttributeError:
        assert True
    except Exception:
        assert False
    try:
        test_obj.director = "NOT Sam VO"
    except AttributeError:
        assert True
    except Exception:
        assert False