# Function = a block of code which is executed only when it is called.

# Function syntax.
def hello(f_name, l_name, age):
	print("Hello " + f_name + l_name)
	print("You are " + str(age) + " years old.")
	print("Have a nice day!")

# Function call - without this the program ignores the function.
# When we call the function we can add arguments - but we need a matching
# numbers of parameters in the function to receive the data.
hello("Just", "Jee", 25)