"""test battery"""

import Calc as calculator

assert calculator.suma(2,3)
assert calculator.suma(-2,3)
assert calculator.suma("a",3)

assert calculator.mult(1,2.23)
assert calculator.mult(0,2)
assert calculator.mult(0,"w")

assert calculator.div(3,5)
assert calculator.div(3,0)
assert calculator.div(0,3)

assert calculator.power(2)
assert calculator.power(-2)
assert calculator.power(0)
assert calculator.power("w")

assert calculator.sqrot(4)
assert calculator.sqrot(0)
assert calculator.sqrot(-4)
assert calculator.sqrot("s")

