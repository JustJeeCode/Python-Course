"""

Scope = The region that a variable is recognized.
		A variable is only available from inside the reigion it is created.
		A global and locally scoped versions of a variable can be created.


name = "Just" 
^^^^^^^^^^^^^
This variable is a global variable (available inside & outside functions.)
Because it was assigned in the main program, not a function.

def display_name():
	name = "Jee"
	^^^^^^^^^^^^
	This variable has local scope because it was
	declared inside of the display_name function (available only inside this function.)

	print(name)


display_name() <- Prints the local variable "Jee"

print(name) <- Will print "Just", because the variable inside of display_name
is a local variable, the print function has no access to it.

"""