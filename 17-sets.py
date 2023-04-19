"""

Set = collection which is unordered, unindexed. No duplicate values.

Set syntax:
utensils = {"fork", "spoon", "knife", "knife", "knife"} 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The duplicate knife values will be removed.

dishes = {"bowl", "plate", "cup", "knife"}

Set functions:

Adds an element:
utensils.add("napkin")

removes a targeted element:
utensils.remove("fork")

clears the set:
utensils.clear()

Adds all elements found in dishes to utensils:
utensils.update(dishes)

Checks what utensils has that dishes doesn't:
print(utensils.difference(dishes))

Checks what utensils and dishes have in common:
print(utensils.intersection(dishes))

Creates a new set with all the elements found in utensils and dishes:
dinner_table = utensils.union(dishes) 

We can loop through all elements in a set just like a list:

for i in dinner_table:
	print(i)
^^^^^^^^^^^^^^^^^^^^^^
Unordered result, will not print duplicate values.

"""