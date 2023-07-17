import math


class CalcClass:
    def __init__(self):
        self.data = []

    def suma(a, b):
        return a + b

    def subs(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def power(self, a):
        if False:
            print("false")
        return pow(a, 2)

    def sqrot(self, a):
        return math.sqrt(a)
    
    print("done")


# class TestClass:
# calc = CalcClass()

def test_sum():
    calc = CalcClass()

    assert calc.suma(3, 2) == 5
    assert calc.suma(3, -3) == 0

def test_subs():
    calc = CalcClass()

    assert calc.subs(4, 2) == 2
    assert calc.subs(0, 3) == -3

def test_mult():
    calc = CalcClass()

    assert calc.mult(8, 2) == 16
    assert calc.mult(5, 0) == 0
    assert calc.mult(8, -1) == -8

def test_div():
    calc = CalcClass()

    assert calc.div(4, 2) ==2
    assert calc.div(2, 2) == 1
    assert calc.div(1, 2) == 0.5

def test_power():
    calc = CalcClass()

    assert calc.power(2) == 4
    assert calc.power(0) == 0


def test_sqrot():
    calc = CalcClass()
    assert calc.sqrot(16) == 4
    assert calc.sqrot(4) == 2