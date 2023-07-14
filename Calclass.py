import math


class Calclass:
    def __init__(self):
        self.data = []

    def suma(self, a, b):
        return a + b

    def subs(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def power(self, a):
        return pow(a, 2)

    def sqrot(self, a):
        return math.sqrt(a)

    print("done")


class TestClass:
    calc = Calclass()

    def test_sum(self):
        assert self.calc.suma(3, 2) == 5
        assert self.calc.suma(3, -3) == 0

    def test_subs(self):
        assert self.calc.subs(4, 2) == 2
        assert self.calc.subs(0, 3) == -3

    def test_mult(self):
        assert self.calc.mult(8, 2) == 16
        assert self.calc.mult(5, 0) == 0
        assert self.calc.mult(8, -1) == -8

    def test_div(self):
        assert self.calc.div(4, 2) == 2
        assert self.calc.div(2, 2) == 1
        assert self.calc.div(1, 2) == 0.5

    def test_power(self):
        assert self.calc.power(2) == 4
        assert self.calc.power(0) == 0

    def test_sqrot(self):
        assert self.calc.sqrot(16) == 4
        assert self.calc.sqrot(-4) == 4


# if __name__ == "__main__":

#     c=Calclass()

#     print(c.suma(3,2))
