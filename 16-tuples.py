"""

Tuple = collection which is ordered and unchangeable
		used to group together related data.

Tuple syntax:
student = ("JustJee", 25, "Male")

Tuple functions:

Counts how many of a selected element is in a tuple:
print(student.count("JustJee")) | OUTPUT => 1


Finds the index value of a selected element in a tuple:
print(student.index("Male")) | OUTPUT => 2


We can also go through all index's like lists:

for i in student:
	print(i)

OUTPUT => "JustJee"
		   25
		  "Male"


We can check if a value is in our tuple:

if "JustJee" in student:
	print("JustJee is here.")

"""


