"""

import time

For loop is a statement that will execute it's block of code
a limited amount of times.

While loop = unlimited.
For loop = limited.


SYNTAX:

for (condition):
	code here


EXAMPLE:

 counter
	v        go to
for i in range(10): <- i just stands for index which is just a temporary variable
	print(i+1)

OUTPUT => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


			 start  end  increment
for i in range(50, 100+1, 2):
	print(i)

OUTPUT => 50, 52, 54, 56... 98, 100


We can iterate through data too. Here is a string.
Each character counts as an index.

for i in "JustJeeCode":
	print(i)

OUTPUT => "J, u, s, t, j, e, e, c, o, d, e" 

	variable
   	   v	      
for seconds in range(10, 0, -1): <- We are counting down.
	print(seconds)
	time.sleep(1)

print("Happy New Year!")

OUTPUT => 10, 9, 8... 2, 1, "Happy New Year!"

