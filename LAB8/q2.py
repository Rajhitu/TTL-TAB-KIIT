# multilevel inheritance
# factory--->wholesale--->retailer

class Factory:
    def __init__(self, name):
        self.name = name

    def produce(self):
        print(f"{self.name} is producing")

class Wholesale(Factory):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

    def ship(self):
        print(f"{self.name} is wholrsaling from {self.location}")

class Retailer(Wholesale):
    def __init__(self, name, location, storefront):
        super().__init__(name, location)
        self.storefront = storefront

    def sell(self):
        print(f"{self.name} is selling from {self.storefront}")

    def print_det(self):
        super().produce();
        super().ship();
        self.sell();

        

# Example usage:
# factory = Factory("My Factory")
# factory.produce()

# # wholesale = Wholesale("My Wholesale", "My Location")
# # wholesale.produce()
# # wholesale.ship()

retailer = Retailer("My Factory", "My Location", "My Storefront")
# retailer.produce()
# retailer.ship()
# retailer.sell()         
retailer.print_det()