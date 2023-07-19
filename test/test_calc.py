# """test battery"""

from Calclass import calclass 
calculator=calclass

def test_sum():
    assert calculator.suma(2,3)
    assert calculator.suma(-2,3)
    assert calculator.suma(0,3)==3

def test_subs():

    assert calculator.subs(2,3)==-1

def test_mult():
    assert calculator.mult(1,2)==2
    assert calculator.mult(0,2)==0
    assert calculator.mult(1,5)==5


def test_div():
    assert calculator.div(6,3)==2
    assert calculator.div(3,1)==3
    assert calculator.div(1,2)==0.5

def test_power():
    assert calculator.power(2)==4
    assert calculator.power(-2)==4
    assert calculator.power(1)==1
    assert calculator.power(8)==64

def test_sqrot():
    assert calculator.sqrot(4)==2
    assert calculator.sqrot(9)==3
    assert calculator.sqrot(16)==4
    assert calculator.sqrot(25)==5

print("Done!")

