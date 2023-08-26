#     employee(emp id,age ,name)
#            /   \
#           /     \
#          /       \
#         /         \
#       regular      daily
#       employe      worker(no of days,wage/day,
#   ( basic ,da,        ot ,total_salary)
#     ta,gross)


class Employee:
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age

    def display(self):
        print("Emp id: ", self.emp_id)
        print("Name: ", self.name)
        print("Age: ", self.age)
        
class RegularEmployee(Employee):
    def __init__(self, emp_id, name, age, basic_salary, da, hra):
        super().__init__(emp_id, name, age)
        self.basic_salary = basic_salary
        self.da = da
        self.hra = hra

    def display(self):
        super().display()
        print("Basic salary: ", self.basic_salary)
        print("DA: ", self.da)
        print("HRA: ", self.hra)

class DailyWorker(Employee):
    def __init__(self, emp_id, name, age, rate_per_day, no_of_days):
        super().__init__(emp_id, name, age)
        self.rate_per_day = rate_per_day
        self.no_of_days = no_of_days

    def display(self):
        super().display()
        print("Rate per day: ", self.rate_per_day)
        print("No of days: ", self.no_of_days)
        
#
print("Press R if u are Regualar Worker :\n ")
print("Press E if u are Regualar Worker :\n ")

n=input()

if(n=='R'):
    regualr=RegularEmployee("2002053","Hitu","20","20lac","20009","211212");
    regualr.display();
else:
    daily=DailyWorker("2002053","Hitu","20","20lac","30");
    daily.display();
