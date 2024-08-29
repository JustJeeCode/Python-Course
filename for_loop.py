# for loops = execute a block of code a fixed number of times.
#			  can iterate over a range, string, sequence, etc.


# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
# 	print(x)


# for x in range(1, 21):
# 	if x == 13:
# 		continue # to skip over an interation
# 	else:
# 		print(x)


for x in range(1, 21):
	if x == 13:
		break # to break out of the loop
	else:
		print(x)