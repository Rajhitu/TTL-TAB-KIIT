# wap class to check an instance belong to a particular class or not and 
# a class belongs to another class or not


class A:
    def __init__(self):
        pass

class B(A):

    def __init__(self) :
        pass


obj=B()
print(F"is  object  belings to B--->{ isinstance(obj,B)}")
print(F"is B a subclass--->{issubclass(B,A)}")