# super() = Function used in a child class to call methods from a parent class (superclass)
#			Allows you to extend the functionality of the inherited methods


class Shape:
	def __init__(self, colour, filled):
		self.colour = colour
		self.filled = filled

	def describe(self):
		print(f"It is {self.colour} and {'filled' if self.filled else 'not filled'}.")


class Circle(Shape):
	def __init__(self, colour, filled, radius):
		super().__init__(colour, filled)
		self.radius = radius

	def describe(self):
		super().describe()
		print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm.")


class Square(Shape):
	def __init__(self, colour, filled, width):
		super().__init__(colour, filled)
		self.width = width

	def describe(self):
		super().describe()
		print(f"It is a square with an area of {self.width * self.width}cm.")



class Triangle(Shape):
	def __init__(self, colour, filled, width, height):
		super().__init__(colour, filled)
		self.width = width
		self.height = height

	def describe(self):
		super().describe()
		print(f"It is a triangle with an area of {self.width * self.height / 2}cm.")


circle = Circle(colour="Red", filled=True, radius=4)
square = Square(colour="Blue", filled=False, width=6)
triangle = Triangle(colour="Yellow", filled=True, width=4, height=6)

# print(circle.colour)
# print(circle.filled)
# print(f"{circle.radius}cm")

# print(square.colour)
# print(square.filled)
# print(f"{square.width}cm")

# print(triangle.colour)
# print(triangle.filled)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")

# circle.describe()
# square.describe()
triangle.describe()

