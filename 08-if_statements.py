"""

If statement = 
A block of code that will execute if the condition is true.

SYNTAX:

If ():
^^^^^^
If (our condition):
	code here.

Here is an example of an if statement:


age = int(input("How old are you?: ")) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here we are assigning the variable age to an integer input.

Here we are checking if age is equal to 100. If it is it will run 
the code inside of the if statement:

if age == 100:
	print("You are a century old!").

Here we are checking else if age is greater or equal to 18. If it is 
it will run the code inside of the elif statement:

elif age >= 18:
	print("You are an adult!")

Here we are checking else if age is less than 0. If it is 
it will run the code inside of the elif statment:

elif age < 0:
	print("You haven't been born yet!")

Here we are using an else statement which will run if the
other if and else if statements result in false.
If our age isn't equal to 100, greater or equal to 18 and less
than 0 do this:

else:
	print("You are a child!")

"""