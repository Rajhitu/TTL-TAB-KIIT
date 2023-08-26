# writea a pyhton class call inventoruy with attributs like item id , item name stalk count and price
#   define suitable methods and constructor to perform opperations like
# add item
# update item
# check item details etc

class inventory:
    item_id = []
    item_name = []

    def __init__(self, item_id, item_name, stock_count, price):
        self.item_id.append(item_id)
        self.item_name.append(item_name)
        self.stock_count = stock_count
        self.price = price

    def add_item(self, itemid, item):
        self.item_id.append(itemid)
        self.item_name.append(item)

    def update_stock(self, new_stock):
        self.stock_count = new_stock

    def check_item(self):
        print("Item id:", self.item_id)
        print("Item name:", self.item_name)
        print("Stock count:", self.stock_count)
        print("Price:", self.price)


i = inventory(0, "", 0, 0)
print("1. Add item")
print("2. Update stock")
print("3. dis[lay item")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = input("enter new item id")
        name = input("enter new item naem")
        i.add_item(id, name)
    elif choice == 2:
        n=input("enter new stock")
        i.update_stock(n)
    elif choice == 3:
        i.check_item()
   
    else:
        print("Invalid choice")
        break;
