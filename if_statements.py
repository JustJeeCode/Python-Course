# If statement = a block of code that will execute if the condition is true.

age = int(input("How old are you?: "))

# == checks if both values are equal.
if age == 100:
	print("You are a century old!")
# >= checks if the left value is greater or equal to the right value.
elif age >= 18:
	print("You are an adult!")
# < checks if the left value is less then the right value.
elif age < 0:
	print("You haven't been born yet!")
# else is just if all the other statements result in false it runs.
else:
	print("You are a child!")