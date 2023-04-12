# scope = The region that a variable is recognized.
#		  A variable is only available fomr inside the reigion it is created.
#		  A global and locally scoped versions of a variable can be created.


name = "Just" # This variable is a global variable (available inside & outside functions.)

def display_name():
	# This variable has local scope to the display_name function because it was
	# declared inside of it (available only inside this function.)
	name = "Jee"
	print(name)

display_name() # Prints the local variable before scoping to the global.
print(name) # Will print "Just".