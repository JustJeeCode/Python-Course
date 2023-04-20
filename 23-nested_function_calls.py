"""

Nested function calls = Function calls inside other function calls.
						Innermost function calls are resolved first.
						Returned value is used as argument for the next outer function.


Standard way:

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num) | OUTPUT => Prints a whole positive number.


Nested function call:

Our input returns to the float that resolves, then so forth with our other outer functions.
We call input -> float -> abs -> round -> print:

print(round(abs(float(input("Enter a whole positive number: ")))))

OUTPUT => Prints a whole positive number.

"""