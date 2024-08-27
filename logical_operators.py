# Logical operators = evaluate multiple conditions (or, and, not)
#					  or = atleast one condition True
#					  and = both conditions True
#					  not = inverts condition (not False, not True)

# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
# 	print("The outdoor event is cancelled.")
# else:
# 	print("The outdoor event is still on!")

temp = 25
is_sunny = False

if temp >= 28 and is_sunny:
	print("It is HOT outside")
	print("and it is SUNNY!")
elif temp <= 0 and is_sunny:
	print("It is COLD outside")
	print("and it is SUNNY!")
elif 28 > temp > 0 and is_sunny:
	print("It is WARM outside")
	print("and it is SUNNY!")
elif temp >= 28 and not is_sunny:
	print("It is HOT outside")
	print("and it is CLOUDY!")
elif temp <= 0 and not is_sunny:
	print("It is COLD outside")
	print("and it is CLOUDY!")
elif 28 > temp > 0 and not is_sunny:
	print("It is WARM outside")
	print("and it is CLOUDY!")
