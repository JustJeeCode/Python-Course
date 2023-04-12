"""

Input allows us to call for an input in the console.

It's best practice to assign them to a variable otherwise there 
would be no stored data from the input.

SYNTAX:

input() <- Also to submit an input you need to press 'ENTER'

ASSIGNING IT TO A VARIABLE:

name = input()


Here we are assigning the variable name to the input "What is your name?: ".
Also by default our input will store as a string value.
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
name = input("What is your name?: ") | OUTPUT => "What is your name?: _"

Here we are assigning the variable age to the integer input "How old are you?: ".
Our input will store as an integer.
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
age = int(input("How old are you?: ")) | OUTPUT => "How old are you?: _"

Here we are assigning height to the float input "How tall are you?: ".
Our input will store as a float.
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
height = float(input("How tall are you?: ")) OUTPUT => "How tall are you?: _"


print("Hello " + name) | OUTPUT => "Hello [name]"

print("You're " + str(age) + " years old.") | OUTPUT => "You're [AGE] years old."
print("You're " + str(height) + "cm tall.") | OUTPUT => "You're [HEIGHT] cm tall."

"""


