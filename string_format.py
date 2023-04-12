# Str.format() = Optional method that gives users more
#				 control when displaying output.


animal = "cow"
item = "moon"

# Standard way to format strings:
# print("The " + animal + " jumped over the " + item)

# format() method:
# print("The {} jumped over the {}".format("cow", "moon"))
# We can also replace the positional arguments with variables.
# {} is a format field they act as a placeholder for our postional arguments.
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) # positional argument
# We can also use keyword arguments in the format() method.
# print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon")) # keyword argument
# We can reuse index's in positional arguments and variables in keyword arguments. 

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Jee"

# We can add padding
print("Hello, my name is {}".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))
print("Hello, my name is {0:>10}. Nice to meet you".format(name))
print("Hello, my name is {name:>10}. Nice to meet you".format(name="James"))

number = 3.14159

print("The number pi is {:.3f}".format(number)) # rounds it.

number = 1000

print("The number pi is {:,}".format(number)) # adds a , after every 1000.
print("The number is {:b}".format(number)) # binary version.
print("The number is {:o}".format(number)) # octil version.
print("The number is {:X}".format(number)) # hexadecimal version (lowercase x for lower, capital x for upper.)
print("The number is {:e}".format(number)) # scientific notation (lower e for lower, capital e for upper.)






