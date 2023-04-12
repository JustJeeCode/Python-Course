# Logical operators (and, or, not) = used to check if two or more conditional
# statements

temp = int(input("What is the temperature outside?: "))

# And, or logical operators.
# if temp >= 0 and temp <= 30:
# 	print("The temperature is good today, go outside.")
# elif temp < 0 or temp > 30:
# 	print("The temperature is bad today, stay inside.")

if not(temp >= 0 and temp <= 30):
	print("The temperature is bad today, stay inside.")
# Or logical operator.
elif not(temp < 0 or temp > 30):
	print("The temperature is good today, go outside.")