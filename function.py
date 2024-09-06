# function = A block of reusable code
# 		     place () after the function name to invoke it

# def happy_birthday(name, age):
# 	print(f"Happy birthday to {name}!")
# 	print(f"You are {age} years old!")
# 	print("Happy birthday to you!")
# 	print()

# happy_birthday("JustJee", 20)
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)

# def display_invoice(username, amount, due_date):
# 	print(f"Hello {username}")
# 	print(f"Your bill of ${amount:.2f} is due: {due_date}.")

# display_invoice("Joe", 100.01, "01/01")

# return = statement used to end a function
#		   and send a result back to the caller

# def add(x, y):
# 	z = x + y
# 	return z

# def subtract(x, y):
# 	z = x - y
# 	return z

# def multiply(x, y):
# 	z = x * y
# 	return z

# def divide(x, y):
# 	z = x / y
# 	return z

# print(divide(1, 2))

def create_name(first, last):
	first = first.capitalize()
	last = last.capitalize()
	return first + " " + last

full_name = create_name("john", "smith")
print(full_name)




