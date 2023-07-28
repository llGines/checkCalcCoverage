# """test battery"""

from mycalc import Calclass1 as cal1
from mycalc import Calclass2 as cal2
from mycalc import Calclass3 as cal3


def test_func():
    assert cal1.suma(2, 3) == 5
    assert cal2.suma(-2, 3) == 1
    assert cal3.suma(0, 3) == 3

    assert cal1.subs(8, 3) == 5
    assert cal2.subs(8, 3) == 5
    assert cal3.subs(8, 3) == 5

    assert cal1.mult(1, 2) == 2
    assert cal2.mult(2, 2) == 4
    assert cal3.mult(1, 5) == 5

    assert cal1.div(3, 6) == 0.5
    assert cal2.div(3, 1) == 3
    assert cal3.div(1, 2) == 0.5

    assert cal1.power(2) == 4
    assert cal2.power(-2) == 4
    assert cal3.power(1) == 1
    

    assert cal1.sqrot(4) == 2
    assert cal2.sqrot(9) == 3
    assert cal3.sqrot(9) == 3
    


print("DONE")
