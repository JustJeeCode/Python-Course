"""
File detection in Python.


EXAMPLE:

import os <- We need the os module.


Here we are getting our path:

path = "/Users/michellestanley/Documents/Python/Course/30-file_detection/folder"


if os.path.exists(path): <- If our path exists.
	print("That location exists!") 
	if os.path.isfile(path): <- If our path is a file.
		print("That is a file!")
	elif os.path.isdir(path): <- If our path is a directory.
		print("That is a directory!")


If our path doesnt exist:

else:
	print("That location doesn't exist!")


"""