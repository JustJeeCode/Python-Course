# Iterables = An object/collection that can return its elements one at a time,
# 			  allowing it to be iterated over in a loop.


# numbers = (1, 2, 3, 4, 5) # works with lists too

# for number in numbers:
# 	print(number)


# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
# 	print(fruit)


# name = "Just Jee"

# for char in name:
# 	print(char, end=" ")


my_dict = {"A": 1,
		   "B": 2,
		   "C": 3}

# for key in my_dict: # for keys
# 	print(key)

# for value in my_dict.values(): # for values
# 	print(value)

for key, value in my_dict.items(): # for both
	print(f"{key} = {value}")