# Keyword arguments = arguments preceded by an identifier, when we pass them to a function. 
#					  The order of the arguments doesn't matter, unlike positional arguments
#					  Python knows the names of the arguments that our function receives.

def hello(first, middle, last):
	print("Hello " + first + " " + middle + " " + last)

# hello("Code", "Jee", "Just") Here the order matters so our first argument = "Code"
# and our last argument = "Just" which is the wrong way round.

hello(last="Code", middle="Jee", first="Just") # Here we ordered them wrong but since
# we are using keyword arguments our first argument = "Just" and our last = "Code" which
# is the right way round. :)