"""

A variable is a container for a value. Behaves as the value that it contains.

EXAMPLE: x = y <- x is the variable and y is the value.

We can store a variable as 4 main data types:

String or Str = which is text (wrapped in quotation marks.)
EXAMPLE: "hi"

Integer or Int = a whole number can be positive or negative (no quotation marks.)
EXAMPLE: 4

Float = a decimal number can be positive or negative (no quotation marks.)
EXAMPLE: 6.424

Boolean or Bool = a true or false value (no quotation marks.)
EXAMPLE: True


STRINGS:

first_name = "Just" 
^^^^^^^^^^^^^^^^^^^
Here we are assigning the variable first_name to the string "Just".

last_name = "Jee"
^^^^^^^^^^^^^^^^^
Here we are assigning the variable last_name to the string "Jee".

full_name = first_name + " " + last_name | Assigning full_name to the string "Just Jee".
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For our variable full_name we are using concatenation.
Concatenating means obtaining a new string that contains both of the original strings. 
In Python, there are a few ways to concatenate or combine strings. 
The new string that is created is referred to as a string object. 
In order to merge two strings into a single object, you may use the + operator.

print("Hello " + full_name) | OUTPUT => "Hello Just Jee"
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here we are now printing to the console the string. So we will be able to see
this text.

print(type(name)) | OUTPUT => str
^^^^^^^^^^^^^^^^^
If we ever want to find the data type of a variable we can use
the type() function.


INTEGERS:

age = 20
^^^^^^^^
We are assigning age to the data type integer and the value is 20.

age += 1
^^^^^^^^
We can add to our integer age with the += operator.

print("Your age is: " + str(age)) | OUTPUT => "Your age is: 21"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here we are type casting our integer variable age to a string. Type casting means
to change the data type of a variable. In print statements you cannot print a string
and any other data type together, so we are type casting our integer variable age to a 
string. Since our type cast is in a print statement however this is not a permanent 
change to age and only effects the variable age in the print statement.

print(type(age)) | OUTPUT => int (type cast wasn't a permanent change.)


FLOATS:

height = 250.5 
^^^^^^^^^^^^^^
We are assigning height to the data type float and the value is 250.5.

print("Your height is: " + str(height) + "cm") | OUTPUT => "Your height is: 250.5cm"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We are concatenating our height variable and type casting its type to a string 
just for the print statement.

print(type(height)) | OUTPUT => float


BOOLEANS:

human = True 
^^^^^^^^^^^^
We are assigning human to the boolean value: True

print("Are you a human: " + str(human)) | OUTPUT => "Are you a human: True"

print(type(human)) | OUTPUT => bool

"""