import math

class Calc():

    """this is just a mere class to try several aspects needed for ipronics job"""
    
    def __init__(self):
        result=0
    
    def suma (self,a,b):
        return a+b
    def subs (a,b):
        return a-b
    def mult (a,b):
        return a*b
    def div (a,b):
        return (a/b)
    def power (a):
        return pow(a,2)
    def sqrot(a):
        return  math.sqrt(a)

        


if __name__ == "__main__":

    c=Calc()

    print(c.suma(3,2))

        

    