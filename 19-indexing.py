# Index operator [] = gives access to a sequence's element (str, list, tuples, etc.)

name = "just Jee!"

# if 'J' is lower.
#if name[0].islower():
	# Capitalizing our name.
	# name = name.capitalize()

# If our index starts at 0 we can leave it blank.
first_name = name[:4].upper()
# If our index goes all the way to the end we can leave it blank.
last_name = name[5:].lower()
# If we want to get the last character we can use a negative index.
last_character = name[-1] # -2 = 'e'

print(first_name)
print(last_name)
print(last_character)
