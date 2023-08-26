class vehicle:
    fare=0
    def __init__(self,fare):
        self.fare=fare
    def checkinstance(self):
        if (isinstance(self,vehicle)):
            self.fare+=self.fare*0.1
        else:
            self.fare+=self.fare*100
    def print_fare(self):
            print(f"total fare {self.fare}")


class bus(vehicle):

    def __init__(self, fare):
        super().__init__(fare)
    def checkinstance(self):
        if (isinstance(self,vehicle)):
            self.fare+=self.fare*0.1
        else:
            self.fare+=self.fare*100
    def print_fare(self):
        print(f"total fare {self.fare}")


# obj=bus(100)
# obj.checkinstance()
# obj.print_fare()

obj=vehicle(100)
obj.checkinstance()
obj.print_fare()