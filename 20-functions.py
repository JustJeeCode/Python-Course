"""

Function = a block of code which is executed only when it is called.


Function syntax:

def is the function call, hello is the variable,
then in the brackets we can put in any arguments these are
just variables. Then we end with a colon.

def hello(f_name, l_name, age):
	print("Hello " + f_name + l_name)
	print("You are " + str(age) + " years old.")
	print("Have a nice day!")

Function call - without this the program ignores the function.
When we call the function we can add arguments - but we need a matching
numbers of parameters in the function to receive the data.

Function call:
hello("Just", "Jee", 25)

Here f_name = "Just", l_name = "Jee" and age = 25.
The position of our data matters, if we switched the positions
of "Just" and "Jee" our first name would be "Jee" and our last name
would be "Just". 

This is called positional arguments.

OUTPUT => "Hello JustJee"
		  "Your are 25 years old."
		  "Have a nice day!"