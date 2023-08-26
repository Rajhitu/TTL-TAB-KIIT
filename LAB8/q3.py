# univerity(regno)       school(roll,name)
#   |                 |    
#   |                 |
#    \               /
#     \             / 
#      \           /
#         student


class University:
    def __init__(self, uniname):
        self.uname = uniname

    def enroll(self):
        print(f"Studieing in {self.uname}")

class School:
    def __init__(self, skolname):
        self.sname = skolname

    def enroll(self):
        print(f"Studied at {self.sname}...")

class Student(University,School):
    def __init__(self, uniname,skolname, program):
        University.__init__(self, uniname)
        School.__init__(self,skolname)
        self.program = program

    def prnt_det(self):
        # print(f"Studying {self.program} at schol{self.name}")
        School.enroll(self);
        University.enroll(self);
        

# Example usage:
student = Student("KIIT","DAV" ,"Computer Science")
student.prnt_det()
# student.study()