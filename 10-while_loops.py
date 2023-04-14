"""

While loop is a statement that will execute it's block of code,
as long as it's condition remains true.

SYNTAX:

while (condition) == True:
	code here

If the condition is a boolean variable True we do not need to write
== True:

while (boolean variable):
	code here


EXAMPLE:

name = None

While our name => nothing -> do whats in our while loop.

while not name:
	name = input("Enter your name: ")

print("Hello " + name)
^^^^^^^^^^^^^^^^^^^^^^
This print statement is outside of the
while loop and will print after the while loop is broken.

"""