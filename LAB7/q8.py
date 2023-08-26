# write a pyhton class called bank account withh attributes like acc no, balance ,cust naem with methods like depost , withdraw and check balance and also print the values

class bank_account :
    # acc_no=0
    # balance=0
    # cust_name=""
    def  __init__(self,name,acc,bal):
         self.acc_no=acc
         self.balance=bal
         self.cust_name=name
        
    def deposit(self,rupee):
        self.balance+=rupee
        print("account credited with Rs "+str(rupee))
    
    def withdraw(self,rupee):
        if self.balance>=rupee:
          self.balance-=rupee
          print("account debited with Rs "+str(rupee))
        else:
            print("print balnce insufficient")
    def print_details(self):
        
            print(F"NAME: {self.cust_name}")
            print(self.acc_no)
            print(self.balance)


obj1=bank_account("hitu",21413,10000)
print("ACCOUNT DETAILS:")
obj1.print_details()
obj1.deposit(1000)
obj1.print_details()
obj1.withdraw(500)
obj1.print_details()
