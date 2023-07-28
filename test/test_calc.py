# """test battery"""

from mycalc import Calclass1, Calclass2, Calclas3 as calculator


def test_func():
    assert calculator.suma(2, 3) == 5
    assert calculator.suma(-2, 3) == 1
    assert calculator.suma(0, 3) == 3

    assert calculator.subs(8, 3) == 5

    assert calculator.mult(1, 2) == 2
    assert calculator.mult(2, 2) == 4
    assert calculator.mult(1, 5) == 5

    assert calculator.div(3, 6) == 0.5
    assert calculator.div(3, 1) == 3
    assert calculator.div(1, 2) == 0.5

    assert calculator.power(2) == 4
    assert calculator.power(-2) == 4
    assert calculator.power(1) == 1
    assert calculator.power(8) == 64

    assert calculator.sqrot(4) == 2
    assert calculator.sqrot(9) == 3
    assert calculator.sqrot(9) == 3
    assert calculator.sqrot(25) == 5


print("DONE")
