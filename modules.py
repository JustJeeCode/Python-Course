# Module = a file containing code you want to include in your program
#		   use 'import' to include a module (built-in or your own)
#		   useful to break up a large program reusable seperate files


# print(help("modules"))
# print(help("math"))

# import math
# import math as m
# from math import pi
# from math import e # not the best practice

# print(e)

# a, b, c, d, e = 1, 2, 3, 4, 5

# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)
# print(e ** e)


import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)