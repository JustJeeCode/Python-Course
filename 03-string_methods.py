"""

String functions in Python.
Here are some functions we can apply to strings in Python.

name = "justJee" <- Example string.

Finds the length of a string:
print(len(name)) | OUTPUT => 7

Finds the place of a given letter:
print(name.find('t')) | OUTPUT => 3 (Computers start counting at 0 >:( )

Capitalizes the first letters of words in a string.
print(name.capitalize()) | OUTPUT => "Justjee" <- makes jee lower because it's all one word.

Capitalizes all letters in a string.
print(name.upper()) | OUTPUT => "JUSTJEE"

Puts all letters in a string in lower case.
print(name.lower()) | OUTPUT => "justjee"

Checks if the string is a number.
print(name.isdigit()) | OUTPUT => False

Checks if the string is only letters.
print(name.isalpha()) | OUTPUT => True

Counts how many of a given letter is in the string.
print(name.count('J')) | OUTPUT => 2

Replaces all letters from a  given letter with another given letter.
print(name.replace("J","R")) | OUTPUT => "rustRee"

Prints the string by x number of times.
print(name * 3) | OUTPUT =>  "justJeejustJeejustJee"

"""