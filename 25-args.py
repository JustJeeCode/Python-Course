"""

*args = parameter that will pack all arguments into a tuple
        useful so that a function can accept a varying amount of arguments.


STANDARD FUNCTION PARAMETERS:

def add(num1, num2):
 	return num1 + num2

print(add(1, 2)) <- Issue with this add function is we cannot add any extra arguments.


*args FUNCTION PARAMETER:

With the * we are packing all the arguments into a tuple defined as "args":

def add(*args):
	sum = 0

	for i in args:
		sum += i

	return sum

print(add(1, 2, 3, 4, 5, 6)) <- We can now pass as many parameters as we want.

OUTPUT => 21

"""
