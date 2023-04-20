"""
**kwargs = Parameter that will pack all arguments into a dictionary
           useful so that a function can accept a varying amount of keyword arguments.

** packs all key, value pairs into our dictionary defined as "kwargs".
kwargs is just the name of our dictionary, we can change it.

def hello(**kwargs):
	print("Hello " + kwargs['first'] + " " + kwargs['last'])
	print("Hello", end = " ")

	for key, value in kwargs.items():
		print(value, end = " ")

Packs all keyword arguments into key, value pairs into the kwargs dictionary:

hello(title = "Mr", first = "Just", middle = "Jee", last = "Code") 

OUTPUT => "Hello Just Code"
		  "Hello Mr Just Jee Code"