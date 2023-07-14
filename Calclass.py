import math

class Calclass():

    """this is just a mere class to try several aspects needed for ipronics job"""
    
    
    # def __init__(self):
    #     result=0
    
    def suma (self,a,b):
        return a+b
    def subs (self, a,b):
        return a-b
    def mult (self, a,b):
        return a*b
    def div (self, a,b):
        return (a/b)
    def power (self,a):
        return pow(a,2)
    def sqrot(self, a):
        return  math.sqrt(a)


        
class TestClass:
    calc=Calclass()
    
    def test_sum(self):
    
        assert calc.suma(3,2)
        assert calc.suma(3,-3)==0
    
    def test_subs(self):
        assert calc.subs(4,2)==2
        assert calc.subs(0,3)==3

    def test_mult(self):
        assert calc.mult(8,2)==16
        assert calc.mult(5,0)==0
        assert calc.mult(8,-1)=-8
    
    def test_div(self):
        assert calc.dev(4,2)==2
        assert calc.dev(2,2)==0
        assert calc.dev(1,2)==0.5

    def test_power(self):
        assert calc.power(2)==4
        assert calc.power(0)==0
    def test_sqrot(self):
        assert calc.sqrot(16)==4
        assert calc.sqrot(-4)==4





# if __name__ == "__main__":

#     c=Calclass()

#     print(c.suma(3,2))

        

