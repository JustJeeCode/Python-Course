# 2D lists = a list of lists.

# Here are our 3 lists.
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

# Here is our 2D list food and inside it are all 3 of our lists.
food = [drinks, dinner, dessert]

# Prints all the elements in every list.
print(food)

# If we wanna access just 1 list we can use the index.
print(food[0])

# If we wanna access an element from inside a list.
print(food[0][0])