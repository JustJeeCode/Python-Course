
# fruits = 	 ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = 	 ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries[2][1])


# groceries = [["apple", "orange", "banana", "coconut"],
# 			 ["celery", "carrots", "potatoes"],
# 			 ["chicken", "fish", "turkey"]]
# 			 # can also be made of tuples and sets

# # for collection in groceries: # only iterates over rows
# # 	print(collection)

# for collection in groceries:
# 	for food in collection: # nested loops iterate rows and cols
# 		print(food, end=" ")
# 	print()


num_pad = ((1, 2, 3),
		   (4, 5, 6),
		   (7, 8, 9),
		   ("*", 0, "#"))

for row in num_pad:
	for num in row:
		print(num, end=" ")
	print()
	