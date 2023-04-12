# While loop = a statement that will execute it's block of code,
#			   as long as it's condition remains true.


name = None

# While our name = nothing -> do whats in our while loop.
while not name:
	name = input("Enter your name: ")

print("Hello " + name)