# Variable scope = where a variable is visible and accessible
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


# def func1():
# 	x = 1 # local scope
# 	print(x)

# def func2():
# 	x = 2
# 	print(x)

# func1()
# func2()


# def func1():
# 	x = 1 # enclosed scope

# 	def func2():
# 		print(x)
# 	func2()

# func1()


# def func1():
#  	print(x)

# def func2():
#  	print(x)

# x = 3 	

# func1()
# func2()


from math import e

def func1():
	print(e)

e = 3

func1()
