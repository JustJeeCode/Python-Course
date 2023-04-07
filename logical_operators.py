# logical operators (and, or, not) = used to check if two or more conditional
# statements

temp = int(input("What is the temperature outside?: "))

# and, or logical operators
# if temp >= 0 and temp <= 30:
# 	print("The temperature is good today, go outside.")
# elif temp < 0 or temp > 30:
# 	print("The temperature is bad today, stay inside.")

# not logical operator
if not(temp >= 0 and temp <= 30):
	print("The temperature is bad today, stay inside.")
elif not(temp < 0 or temp > 30):
	print("The temperature is good today, go outside.")