# wap in python with oop concept to inmplement a user defined  queeue data structure then perform insert and remove methods with a set of elemenets

class queuee:
    list = []

    def __init__(self, list):
        self.list = list

    def insert(self, x):
        self.list.append(x)

    def removes(self):
        if (len(self.list) != 0):
            temp=self.list[1:5]
            self.list=temp
        else:
            print("QUEUE IS EMPTY")

    def display(self):
        for i in self.list:
            print(i, end=" ")
        print()


obj = queuee([1, 2, 3, 4])
while 1:
    print("Press1 to push in queue")
    print("Press 2 to pop from queue")
    print("Press 3 to display a ques")
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
