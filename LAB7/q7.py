# write a apython clas call resturant with attributes like menu_items ,book_table, customer order or desgin suitable methods to perform the following 
# 1. add items to the menu 
# 2. make reservation
# 3. take customer order
# 4. print all
# use dictionary and list to store the data 

class resturant:
    # menu_items=["water"]
    # book_table=0
    # customer_order=["water"]

    def __init__(self,item,book,order):
        self.menu_items=item
        self.book_table=book
        self.customer_order=order

    def add_items(self,item):
        self.menu_items.append(item)
        print("items added to menu uccessfuly")
        self.print_det()
        # print("-------------------------------------")
        


    def make_reservation(self,book_table):
        self.book_table=1
        print("your table is booked now")
        self.print_det()
        # print("----------------------------------------")


    def do_order(self,order):
        self.customer_order.append(order)
        print("items ordered suessefuly")
        self.print_det()
        # print("-------------------------------------")


    def print_det(self):
        print(f"book status---> {self.book_table}")
        print(f" menu--->{self.menu_items}")
        print(f" order details---> {self.customer_order}\n\n")

obj=resturant(["chowmin","chilli","biryani","roti","tea","coffee"],1,["chowmin","tea"])
obj.make_reservation(1)

obj.add_items("lolipop")

obj.do_order("cofee")
