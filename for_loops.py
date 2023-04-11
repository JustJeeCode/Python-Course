# Time module allows us to access time.
import time

# For loop = a statement that will execute it's block of code
# 		     a limited amount of times.

#			 While loop = unlimited.
# 			 For loop = limited.

# i = index, can be whatever it's just a variable.

# for i in range(10):
# 	print(i+1)

# for i in range(50, 100+1, 2):
# 	print(i)

# We can iterate through data too. Here is a string.
# for i in "JustJeeCode":
# 	print(i)

# 				  start,end,increment
for seconds in range(10, 0, -1):
	print(seconds)
	time.sleep(1)
print("Happy New Year!")

