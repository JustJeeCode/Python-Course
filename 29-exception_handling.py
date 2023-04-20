"""
Exception = Events detected during execution that interrupt the
	        flow of a program.


SYNTAX:

try:
except:
else:
finally:


EXAMPLE:

Inside the try statement we have dangerous code:
try:  
	numerator = int(input("Enter a number to divide: "))
	denominator = int(input("Enter a number to divide by: "))
	result = numerator / denominator <- We have a dangerous equation here.


If the nominator or denominator = 0 which is a mathmatic error, this will catch it 
and execute this block of code:

except ZeroDivisionError as e: <- 'as e' allows us to put our error into a variable.
	print(e) <- Prints the error.
	print("You can't divide by zero.")


If the nominator or denominator isn't a number
this will catch that error and execute the block of code:

except ValueError as e:
	print(e)
	print("You can only divide numbers.")


If any other exception is called this exception statement
will run:

except Exception as e:
	print(e)
	print("There went wrong :(")


If there were no error the else statement runs:

else:
	print(result)


Regardless whether there was an error or not the finally statement runs:

finally:
	print("Thank you for using this program!")

"""


