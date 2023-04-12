# Tuple = collection which is ordered and unchangeable
#		  used to group together related data.

# Tuple syntax:
student = ("JustJee", 25, "Male")

# Tuple functions:
#print(student.count("JustJee")) # Count how many of a value is in a list
#print(student.index("Male")) # Find the index of a value

# We can also go through all index's like lists.
for i in student:
	print(i)

# We can check if a value is in our tuple.
if "JustJee" in student:
	print("JustJee is here.")