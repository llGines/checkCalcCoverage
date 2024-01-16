import pytest
import learn_testing.calc.calculator as calculator


@pytest.mark.parametrize(
    "a,b,r",
    [
        (2, 3, 5),
        (8, 10, 18),
    ],
)
def test_sum_happy_path(a, b, r):
    assert calculator.sum(a, b) == r


@pytest.mark.parametrize(
    "a,b,e",
    [
        (1, "1", TypeError),
        ("1", 1, TypeError),
    ],
)
def test_sum_sad_path(a, b, e):
    pytest.raises(e, calculator.sum, a, b)


@pytest.mark.parametrize(
    "a,b,r",
    [
        (8, 3, 5),
        (8, 10, -2),
    ],
)
def test_subs_happy_path(a, b, r):
    assert calculator.subs(a, b) == r


@pytest.mark.parametrize(
    "a,b,e",
    [
        (1, "1", TypeError),
        ("1", 1, TypeError),
    ],
)
def test_subs_sad_path(a, b, e):
    pytest.raises(e, calculator.subs, a, b)


@pytest.mark.parametrize(
    "a,b,r",
    [
        (1, 2, 2),
        (2, 0, 0),
    ],
)
def test_mult_happy_path(a, b, r):
    assert calculator.mult(a, b) == r


@pytest.mark.parametrize(
    "a,b,e",
    [
        (1, "1", TypeError),
        ("1", 1, TypeError),
    ],
)
def test_mult_sad_path(a, b, e):
    pytest.raises(e, calculator.mult, a, b)


@pytest.mark.parametrize(
    "a,b,r",
    [
        (10, 5, 2),
        (20, 10, 2),
    ],
)
def test_div_happy_path(a, b, r):
    assert calculator.div(a, b) == r


@pytest.mark.parametrize(
    "a,b,e",
    [
        (1, "1", TypeError),
        ("1", 1, TypeError),
        (1, 0, ZeroDivisionError),
    ],
)
def test_div_sad_path(a, b, e):
    pytest.raises(e, calculator.div, a, b)


@pytest.mark.parametrize(
    "a,b,r",
    [
        (10, 2, 100),
        (2, 2, 4),
    ],
)
def test_power_happy_path(a, b, r):
    assert calculator.power(a, b) == r


@pytest.mark.parametrize(
    "a,b,e",
    [
        (1, "1", TypeError),
        ("1", 1, TypeError),
    ],
)
def test_power_sad_path(a, b, e):
    pytest.raises(e, calculator.power, a, b)


@pytest.mark.parametrize(
    "a,r",
    [
        (9, 3),
        (25, 5),
    ],
)
def test_sqrot_happy_path(a, r):
    assert calculator.sqrot(a) == r


@pytest.mark.parametrize(
    "a,e",
    [
        ("1", TypeError),
        (-1, ValueError),
    ],
)
def test_sqrt_sad_path(a, e):
    pytest.raises(e, calculator.sqrot, a)
