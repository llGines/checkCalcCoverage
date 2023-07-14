import math


class Calclass:

    """this is just a mere class to try several aspects needed for ipronics job"""

    # def __init__(self):
    #     result=0

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


class TestClass:
    calc = Calclass()

    def test_sum(self):
        ret = calc.suma(3, 2)
        assert ret == 5


# if __name__ == "__main__":

#     c=Calclass()

#     print(c.suma(3,2))
