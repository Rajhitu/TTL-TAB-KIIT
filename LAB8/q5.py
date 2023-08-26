            #  student
            #    |
            #    |
            #    |
            #   exam                 cocuuricular activity(score)
            #    |                            |
            #    |                            |
            #    |                            |
            #    |____________________________|
            #               |
            #               |
            #               |
            #               |
            #             result



class student:
    name=""
    roll=0
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def print_det(self):
        print(f"name:{self.name}\troll:{self.roll}")
        
        

class exam(student):
    # marks1=0
    # marks2=0
    def __init__(self,marks1,marks2,name,roll):
         super().__init__(name,roll)
         self.marks1=marks1
         self.marks2=marks2

    def print_det(self):
      super().print_det();
      print(f"Marks1:{self.marks1}\troll:{self.marks2}")
     


class cocuuricular_activity:

  
    def __init__(self,activitymarks):
         
         self.activitymarks=activitymarks

    def print_det(self):
      print(f"Marks in activity is :{self.activitymarks}\n")

class result(exam,cocuuricular_activity):
    tmarks=0
    def __init__(self,marks1,marks2,name,roll,activitymarks):
          exam.__init__(self,marks1,marks2,name,roll)
          cocuuricular_activity.__init__(self,activitymarks)
       

    def total_marks(self):
           self.tmarks=self.marks1+self.activitymarks+self.marks2
           print(self.tmarks)

    def print_det(self):
          print(f"Total Marks of the student is :{self.tmarks}\n")
          exam.print_det(self)

obj=result(90,95,"hitu",2000525,88)
obj.total_marks()
obj.print_det()

