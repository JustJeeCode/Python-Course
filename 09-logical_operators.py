"""

Logical operators are operators used to check two 
or more conditional statements.

Logical operators include: and, or, not


SYNTAX:
	
if (condition) or/and if (condition):
	code here.

if not(condition):
	code here.

if not(conditon) or/and if (condition):
	code here.


HERE IS AN EXAMPLE:

temp = int(input("What is the temperature outside?: "))
^^^^
Assigning the variable temp the integer input.

Here we use the and logical operator:
We are basically saying if temp is greater or equal to 0 and
temp is less than or equal to 30 do this.

if temp >= 0 and temp <= 30:
	print("The temperature is good today, go outside.")


Here we are using the or logical operator:
We are basically saying else if temp is less than 0 or temp
is greater then 30 do this.

elif temp < 0 or temp > 30:
	print("The temperature is bad today, stay inside.")


Here we are using the not logical operator:
We are basically saying if temp is NOT greater or equal to 0
and temp is NOT less then or equal to 30 do this.

if not(temp >= 0 and temp <= 30):
	print("The temperature is bad today, stay inside.")


Here we are using the not logical operator:
We are basically saying if temp is NOT less than 0 or temp
is NOT greater than 30 do this.

elif not(temp < 0 or temp > 30):
	print("The temperature is good today, go outside.")

"""