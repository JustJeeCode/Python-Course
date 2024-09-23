# Object = A "bundle" of related attributes (variables) and methods (functions)
#		   Ex. phone, cup, book
#		   You need a "class" to create many objects

# Class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Corvette", 2002, "red", False)
car2 = Car("Lambo", 2022, "yellow", True)
car3 = Car("Mustang", 1999, "black", True)

# print(car3.model)
# print(car3.year)
# print(car3.colour)
# print(car3.for_sale)

# car1.drive()
# car2.drive()
# car2.stop()
# car3.drive()

car3.describe()