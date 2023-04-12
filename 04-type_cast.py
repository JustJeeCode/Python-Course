"""

Type casting = Convert the data type of a value to another data type.

Here we have some variables with there data types.
x = 1 <- int
y = 2.0 <- float
z = "3" <- string

Here we are type casting the variable x which is an integer to a string, this change stays
until we change it back or to another data type.

x = str(x) | this would now be "x" which is a string.

Here we are type casting our variable y which is a float to a string. Since our type cast
is in a print statement however this change is only temporary and after the print 
statement y will still be a float.

print("Y is " + str(y)) | OUTPUT => Y is 2.0

Here we are type casting the string z to an integer then multiplying it by 3.

print(int(z)*3) | OUTPUT => 9

"""