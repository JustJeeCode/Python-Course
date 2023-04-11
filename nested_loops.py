# nested loops = The "inner loop" will finish all of it's iterations before 
# 				 finishing one iteration of the "outer loop"

# gettings rows, columns and symbol
rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# first for loop is the rows
for i in range(rows):
	# nested for loop is the cols, also it's good practice to use a j for 
	# nested for loops
	for j in range(cols):
		# end="" makes the print statement print to the same line
		print(symbol, end=" ")
	# printing a new line for every row
	print()


