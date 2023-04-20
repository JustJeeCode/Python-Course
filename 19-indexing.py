"""

Index operator [] = gives access to a sequence's element 
We can use the index operator in - str, list, tuples, etc.


SYNTAX:

Inside we have a number or
we have a start, stop, step.
 v
[x] <- Number.

[x:y:z] <- Start, stop, step.


EXAMPLE: For a single number.

name = "just Jee!"

if 'J' is lower:
if name[0].islower(): <- name[0] = "j"
	Capitalizing our name.
	name = name.capitalize() <- We are using the capitalize function on our name variable.

OUTPUT => "Just Jee"


EXAMPLE: For start, stop, step.

first_name = name[:4].upper() <- If our index starts at 0 we can leave it blank.

OUTPUT => first_name = "JUST"


last_name = name[5:].lower() <- If our index goes all the way to the end we can leave it blank.

OUTPUT => last_name = "jee"


If we want to get the last character we can use a negative index:
last_character = name[-1] <- An index of [-2] = 'e'

OUTPUT => last_character = "!"

"""
