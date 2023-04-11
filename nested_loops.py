# Nested loops = The "inner loop" will finish all of it's iterations before 
# 				 finishing one iteration of the "outer loop".

# Gettings rows, columns and symbol
rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# First for loop is the rows.
for i in range(rows):
	# Nested for loop is the cols. Also it's good practice to use a j for 
	# nested for loops.
	for j in range(cols):
		# end="" makes the next iteration print to the same line.
		print(symbol, end=" ")
	# Printing a new line for every row.
	print()


