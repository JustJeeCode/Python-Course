"""
Loop Control Statements = change a loops execution from its normal sequence.

break	= 	used to terminate the loop entirely.
continue  = 	skips to the next iteration of the loop.
pass	=	does nothing, acts as a placeholder.


SYNTAX:

break, continue, pass


EXAMPLE -> Example of the break statement:

while True:
	name = input("Enter your name: ")
	if name != "": <- if name doesn't equal nothing.
		break <- break which will end the loop.


EXAMPLE -> Example for the continue statement:

phone_number = "123-456-7890"

for i in phone_number:
	if i == "-": <- if i equals the -
		continue <- continue which will skip to the next iteration.


EXAMPLE -> Example for pass:

for i in range(1, 21):

	if i == 13: <- if i equals 13
		pass <- this code will be ignored.
	else:
		print(i)

	print("hi") <- This code will still run after the pass.








