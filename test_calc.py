# """test battery"""

from Calclass import Calclass 
calculator=Calclass

assert calculator.suma(2,3)
assert calculator.suma(-2,3)
assert calculator.suma(0,3)

assert calculator.mult(1,2.23)
assert calculator.mult(2,2)
assert calculator.mult(1,5)

assert calculator.div(3,5)
assert calculator.div(3,1)
assert calculator.div(1,3)

assert calculator.power(2)
assert calculator.power(-2)
assert calculator.power(1)
assert calculator.power(8)

assert calculator.sqrot(4)
assert calculator.sqrot(3)
assert calculator.sqrot(4)
assert calculator.sqrot(2)

