import pytest
import learn_testing.area.calc_areas as calc_areas
import learn_testing.area.exception_zero as Ng

# Given the next tests, write the code for calculating areas
# that passes them:
# HINT: areas can't have negative values.


@pytest.mark.parametrize(
    "a,b,r",
    [
        (2, 3, 6),
        (8, 10, 80),
    ],
)
def test_square_happy_path(a, b, r):
    assert calc_areas.square(a, b) == r


@pytest.mark.parametrize(
    "a,b,e",
    [
        (1, "1", TypeError),
        ("1", 1, TypeError),
        (-1, 1, Ng.NegativeError),
    ],
)
def test_square_sad_path(a, b, e):
    pytest.raises(e, calc_areas.square, a, b)


@pytest.mark.parametrize(
    "a,b,r",
    [
        (5, 4, 10),
        (6, 4, 12),
    ],
)
def test_triangle_happy_path(a, b, r):
    assert calc_areas.triangle(a, b) == r


@pytest.mark.parametrize(
    "a,b,e",
    [
        (1, "1", TypeError),
        ("1", 1, TypeError),
        (-1, 1, Ng.NegativeError),
    ],
)
def test_triangle_sad_path(a, b, e):
    pytest.raises(e, calc_areas.triangle, a, b)


@pytest.mark.parametrize(
    "a,r",
    [
        (2, 10.39),
        (5, 64.95),
    ],
)
def test_hexagon_happy_path(a, r):
    # r = round(r, 2)
    assert round(calc_areas.hexagon(a), 2) == r


@pytest.mark.parametrize(
    "a,e",
    [
        ("1", TypeError),
        (-1, Ng.NegativeError),
    ],
)
def test_hexagon_sad_path(a, e):
    pytest.raises(e, calc_areas.hexagon, a)


@pytest.mark.parametrize(
    "a,r",
    [
        (3, 28.27),
        (5, 78.54),
    ],
)
def test_circle_happy_path(a, r):
    assert round(calc_areas.circle(a), 2) == r


@pytest.mark.parametrize(
    "a,e",
    [
        ("1", TypeError),
        (-1, Ng.NegativeError),
    ],
)
def test_circle_sad_path(a, e):
    pytest.raises(e, calc_areas.circle, a)
