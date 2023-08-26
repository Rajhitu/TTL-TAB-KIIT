# write a pyhton class naem circleeith attribute radiusand 2 methods that will compute the area and perimtere of the circle
class circle:
    radius = 0.0

    def __init__(self, r): 
        self.radius = r

    def area(self):
        print(f"area of the circle is :{3.14*self.radius*self.radius}")

    def perimter(self, r=radius):
        print(f"perimetr of circle is:{2*3.14*self.radius}")


obj=circle(7)

obj.area()
obj.perimter()