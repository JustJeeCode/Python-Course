# Set = collection which is unordered, unindexed. No duplicate values.

# Set syntax.
utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# Set functions:
# utensils.add("napkin") # Adds an element.
# utensils.remove("fork") # Removes an element.
# utensils.clear() # Clears the set.
# utensils.update(dishes) # Adds all elements found in dishes to utensils.
# print(utensils.difference(dishes)) # Checks what utensils has that dishes doesn't.
# print(utensils.intersection(dishes)) # Checks what utensils and dishes has in common.

# Creates a new set with all the elems found in utensils and dishes.
dinner_table = utensils.union(dishes) 

# We can loop through all elements in a set just like a list.
for i in dinner_table:
	print(i) # Unordered result, will not print duplicate values.