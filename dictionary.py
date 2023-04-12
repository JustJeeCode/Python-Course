# Dictionary = A changeable, unordered, collection of unique key:value pairs
# 			   Fast because they use hashing, allow us to access a value quickly.

# Dictionary syntax.
capitals = {"USA":"Washington DC",
			"India":"New Dehli",
			"China":"Beijing",
			"Russia":"Moscow"}

# How to access a value with a key in a dictionary.
# print(capitals['Russia']) # Not safe, if key doesn't exist it throughs an error.
# print(capitals.get('Germany')) # Safe, if key doesn't exist it outputs None.

# Dictionary functions:
# print(capitals.keys()) # Prints only keys.
# print(capitals.values()) # Prints only values.
# print(capitals.items()) # Prints all items.
capitals.update({"Germany":"Berlin"}) # We can add key, value pairs with update().
capitals.update({"USA":"New York"}) # We can also edit an existing pair with update().
# Changes our key 'USA' to a new value of 'New York'.
capitals.pop("China") # We can remove a key, value pair with pop().
capitals.clear() # Clears the dictionary.

# Another way we can get key, value pairs is by this key, value loop.
for key, value in capitals.items():
	print(key, value)
