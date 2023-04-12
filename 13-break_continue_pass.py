# Loop Control Statements = change a loops execution from its normal sequence.

# break		= 	used to terminate the loop entirely.
# continue	= 	skips to the next iteration of the loop.
# pass		=	does nothing, acts as a placeholder.


# Example for break, we break this while loop when our name
# variable = something.

# while True:
# 	name = input("Enter your name: ")
# 	if name != "":
# 		break

# Example for continue, we continue if == "-"
# to the next iteration of the loop.

# phone_number = "123-456-7890"

# for i in phone_number:
# 	if i == "-":
# 		continue
	
# 	print(i, end="")

# Example for pass, if i == 13, pass to next
# line of code.
for i in range(1, 21):

	if i == 13:
		pass
	else:
		print(i)








