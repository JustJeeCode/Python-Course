# Return statement = Functions send Python values/objects back to the caller.
#					 These values/objects are known as the function's return value.


def multiply(number1, number2):
	# result = number1 * number2 <- We don't need this.
	return number1 * number2 # Return syntax.

x = multiply(6, 8) # We can assign a function to a variable.

print(x)