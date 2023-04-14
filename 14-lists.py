"""

List = used to store multiple items in a single variable.


SYNTAX:

food = ["pizza", "hamburger", "hotdog", "muffin", "pudding"]


We can print or target a specific item of a list with the index
operators:

print(food[4]) | OUTPUT => "pudding"
^^^^^^^^^^^^^^
Remember computers start counting at 0.


We can change items in a list.
We change item 0 to "sushi":

food[0] = "sushi"

print(food[0]) | OUTPUT => "sushi"


Here are some -
List functions:

food.append("ice cream") <- We add ice cream to the end of the list.
food.remove("hotdog") <- We remove hotdog from the list.
food.pop() <- Removes last element.
food.insert(0, "cake") <- Replaces an element with a new one.
food.sort() <- Sorts list alphabetically.
food.clear() <- Removes all elements of a list.

We can print all items of a list to a new line with a for loop:

for i in food:
	print(i)

OUTPUT => "pizza"
		  "hamburger"
		  "hotdog"
		  "muffin"
		  "pudding"

"""