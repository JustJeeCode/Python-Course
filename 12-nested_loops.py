"""

A nested loop is the "inner loop" of 2 for loops, it will finish
all iterations of itself before the outer loop will finish 1
iteration.


SYNTAX:

for (condition):
	code here
	for (condition): <- will finish all iterations
		code here 


EXAMPLE:

Here we will build a brick with rows and columns and a symbol
of our choosing.

rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")


The first for loop is for the rows.
for i in range(rows):
	
	The nested for loop is for the columns and it is common to use
	a j as an index for nested loops.
	for j in range(cols):
		print(symbol, end=" ") <- End keeps printing to the same line.
	print() <- We are printing a new line for every row.

OUTPUT => (let's say we did 2x2 and used the # symbol.)
=> # #
   # #

"""






