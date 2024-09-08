# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#			 * unpacking operator
#			 1. positional 2. default 3. keyword 4. arbitrary


# def add(a, b):
# 	return a + b

# print(add(5, 5))


# def add(*args):
# 	total = 0
# 	for arg in args:
# 		total += arg
# 	return total

# print(add(1, 2, 3, 14, 56, 22))


# def display_name(*args):
# 	for arg in args:
# 		print(arg, end=" ")

# display_name("Mr.", "John", "Stanley", "Doe")


# def print_address(**kwargs):
# 	for key, value in kwargs.items():
# 		print(f"{key}: {value}")

# print_address(street="123 Cheese Street",
# 			  apt="100",
# 			  city="New York City", 
# 			  state="NY", 
# 			  zip="34980")


def shipping_label(*args, **kwargs):
	for arg in args:
		print(arg, end=" ")
	print()

	if "apt" in kwargs:
		print(f"{kwargs.get('street')} {kwargs.get('apt')}")
	elif "pobox" in kwargs:
		print(f"{kwargs.get('street')}")
		print(f"{kwargs.get('pobox')}")
	else:
		print(f"{kwargs.get('street')}")

	print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
			   street="123 Fake St.",
			   pobox="PO box #1001",
			   city="Detroit",
			   state="MI",
			   zip="54321")





