# write a python class to implement pow(x.n)
class pow:
    base=0
    power=0

    def __init__(self,base,pow):
        self.base=base
        self.power=pow
    def calc(self):
        return self.base**self.power
    
obj=pow(2,3)
print(f"power ={obj.calc()}")