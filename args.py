# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments.

# def add(num1, num2):
# 	sum = num1 + num2
# 	return sum

# print(add(1, 2)) Issue with this add function is we cannot add any extra parameters.

# With the * we are packing all the arguments into a tuple defined as "args".
def add(*args):
	sum = 0
	args = list(args) # If we want to change our tuple we can type cast it to a list.
	args[0] = 0

	for i in args:
		sum += i

	return sum

print(add(1, 2, 3, 4, 5, 6)) # We can now pass as many parameters as we want.

