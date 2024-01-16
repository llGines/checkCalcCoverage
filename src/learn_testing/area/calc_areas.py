from learn_testing.area.exception_zero import NegativeError
import math


def square(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    elif a < 0 or b < 0:
        raise NegativeError
    else:
        return a * b


def triangle(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("not integer passed in ", __name__)
    elif a < 0 or b < 0:
        raise NegativeError
    else:
        return a * b / 2


def hexagon(a):
    if not isinstance(a, int):
        raise TypeError("not integer passed in ", __name__)
    elif a < 0:
        raise NegativeError
    else:
        return (3 * math.sqrt(3) / 2) * pow(a, 2)


def circle(a):
    if not isinstance(a, int):
        raise TypeError("not integer passed in ", __name__)
    elif a < 0:
        raise NegativeError
    else:
        return math.pi * pow(a, 2)
