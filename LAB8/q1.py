# wap to use simple inhertance of class bank and customer where customer is derived from bank

class Bank:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance is {self.balance}.")
        else:
            print("Insufficient funds.,cant withdraw")
    
    def print_det(self):
        print(self.name)  
        print(self.account_number) 
        print(self.balance) 


class Customer(Bank):
    def __init__(self, name, account_number, balance, phone_number):
        super().__init__(name, account_number, balance)
        self.phone_number = phone_number


    def get_det(self):
        super().print_det();
        print(f"Phone number: {self.phone_number}.")
    



customer = Customer("hitu raj", "10/10/2002", 1000, "8507250144")

customer.get_det()  
customer.deposit(500)  
customer.withdraw(2000)  
