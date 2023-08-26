# writre a python class name student with 2 instances stuudent 1 and student 2  seclare suitable data members or attribute and member fucntion to initialize display the vlaue of the attributess

class Student:
    # name=""
    # roll=0
    # sec=""

    def __init__(self,name,roll,sec):
        self.name=name
        self.roll=roll
        self.sec=sec

    def print_details(self):
        print(f"name->{self.name}")
        print(f"roll->{self.roll}")
        print(f"sec->{self.sec}")


stud1=Student('hitu',2005025,'cse10')
stud2=Student("rahul",2005217,"cse5")
stud1.print_details()
stud2.print_details()
