"""
.format() = Optional method that gives users more
			control when displaying output.


EXAMPLE:

animal = "cow"
item = "moon"

Standard way to format strings:

print("The " + animal + " jumped over the " + item)

OUTPUT => "The cow jumped over the moon"


Format method:

print("The {} jumped over the {}".format("cow", "moon"))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here we are using the format method to put the text cow in the first {}
and moon in the second {}, this uses positional arguments.

OUTPUT => "The cow jumped over the moon"


We can also replace the positional arguments with variables.
{} is a format field they act as a placeholder for our postional arguments:

print("The {} jumped over the {}".format(animal, item)) <- Variables.

OUTPUT => "The cow jumped over the moon"


We can re-order the positional arguments with indexing:

print("The {1} jumped over the {0}".format(animal, item))

OUTPUT => "The moon jumped over the cow"


We can also use keyword arguments in the format method:

print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon"))

OUTPUT => "The cow jumped over the moon"


We can reuse index's in positional arguments and variables in keyword arguments. 


text = "The {} jumped over the {}"
print(text.format(animal, item)) <- Here we are formatting our variable 'text'.

OUTPUT => "The cow jumped over the moon"


EXAMPLE 2 - PADDING:

name = "Jee"

We can add padding:

print("Hello, my name is {}".format(name)) | OUTPUT => "Hello, my name is Jee"

print("Hello, my name is {:<10}. Nice to meet you".format(name))

OUTPUT => "Hello, my name is Jee       . Nice to meet you"


print("Hello, my name is {:>10}. Nice to meet you".format(name))

OUTPUT => "Hello, my name is        Jee. Nice to meet you"


print("Hello, my name is {:^10}. Nice to meet you".format(name))

OUTPUT => "Hello my name is     Jee     . Nice to meet you"


print("Hello, my name is {0:>10}. Nice to meet you".format(name))

OUTPUT => "Hello, my name is        Jee. Nice to meet you"


print("Hello, my name is {name:>10}. Nice to meet you".format(name="James"))

OUTPUT => "Hello, my name is        James. Nice to meet you"


EXAMPLE 3 - NUMBERS:

number = 3.14159

print("The number pi is {:.3f}".format(number)) <- .3f rounds to 3 decimal places.

OUTPUT => "The number pi is 3.142" <- Rounds up.


number = 1000

print("The number is {:,}".format(number)) <- Adds a , after every 1000.

OUTPUT => "The number is 1,000"


print("The number is {:b}".format(number)) <- Binary version.

OUTPUT => "The number is 1111101000"


print("The number is {:o}".format(number)) <- Octil version.

OUTPUT => "The number is 1750"


print("The number is {:X}".format(number)) <- Hexadecimal version (The capital 'X' capitalizes it.)

OUTPUT => "The number is 3E8"


print("The number is {:e}".format(number)) <- Scientific notation (The lower case 'e' lowers it.)

OUTPUT => "The number is 1.000000e+03"


"""
