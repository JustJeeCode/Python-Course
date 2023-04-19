"""

Dictionary = A changeable, unordered, collection of unique key:value pairs
   		     Fast because they use hashing, allow us to access a value quickly.


Dictionary syntax:

capitals = {"USA":"Washington DC", <- "USA" would be the key and "Washington DC" would be the value.
			"India":"New Dehli",
			"China":"Beijing",
			"Russia":"Moscow"}



How to access a value with a key in a dictionary:

print(capitals['Japan']) | OUTPUT => ERROR <- Not safe, if key doesn't exist it throughs an error.
print(capitals.get('Germany')) OUTPUT => None <- Safe, if key doesn't exist it outputs None.


Dictionary functions:

Prints only the keys:
print(capitals.keys()) | OUTPUT => "USA"
								   "India"
								   "China"
								   "Russia"

Prints only the values:
print(capitals.values()) | OUTPUT => "Washington DC"
									 "New Dehli"
									 "Beijing"
									 "Moscow"

Prints all items:
print(capitals.items()) | OUTPUT => "USA":"Washington DC",
									"India":"New Dehli",
									"China":"Beijing",
									"Russia":"Moscow"

We can add key, value pairs with the update function:
capitals.update({"Germany":"Berlin"}) | OUTPUT => "USA":"Washington DC",
												  "India":"New Dehli",
											   	  "China":"Beijing",
									              "Russia":"Moscow",
									              "Germany":"Berlin"

We can also edit an existing key, value pair with the update function:
capitals.update({"USA":"New York"}) | OUTPUT => "USA":"New York",
												"India":"New Dehli",
												"China":"Beijing",
												"Russia":"Moscow"

We can remove a key, value pair with the pop function:
capitals.pop("China") | OUTPUT => "USA":"Washington DC",
								  "India":"New Dehli",
  								  "Russia":"Moscow"

We can clear the dictionary with the clear function:
capitals.clear() | OUTPUT => {}

Another way we can get key, value pairs is by this key, value loop:
for key, value in capitals.items():
	print(key, value)

OUTPUT => "USA New York"
		  "India New Dehli"
		  "China Beijing"
		  "Russia Moscow"

The first positional variable is always the key, and the second is always the value.
Also we need to access the items function to use our key, value pair.

"""
