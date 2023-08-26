# WAP IN PYTHON with  TO IMPLEMNT USER DISFINED stack DATA STRUCTUREE then demonstrate the push and pop method with a set of element

class stack:
    list = []

    def __init__(self, list):
        self.list = list

    def insert(self, x):
        self.list.append(x)

    def removes(self):
        if (len(self.list) != 0):
           self.list.remove(self.list[-1])
        else:
            print("STACK IS EMPTY")

    def display(self):
        for i in self.list:
            print(i, end=" ")
        print()


obj = stack([1, 2, 3, 4])
while 1:
    print("Press1 to push in STACK")
    print("Press 2 to pop from STACK")
    print("Press 3 to display a STACK")
    n=int(input())
    if (n == 1):
     x=int(input())
     obj.insert(x)
    elif (n == 2):
     obj.removes()
    elif (n == 3):
     obj.display()
    else:
     print("Wrong choice")
     break