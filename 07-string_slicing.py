"""

Slicing = create a substring by extracting elements from another string.
we can slice by -> indexing[] or using the slice() function.

To use an index we call our variable with the [] square brackets after it.

This is the order of our index calls:

[start:stop:step]
^^^^^^^^^^^^^^^^^
We put in our start index, then our stop index, then our step index.

Here is an example:


INDEXING:

name = "JustJeeCode" <- Assigning variable name to the string - "JustJeeCode"

first_name = name[0:7] | OUTPUT => "JustJee"
^^^^^^^^^^^^^^^^^^^^^
Here we are assigning the variable first_name to -> the 1st character of name to
the 7th character.

last_name = name[7:] | OUTPUT => "Code"
^^^^^^^^^^^^^^^^^^^^
Here we are assigning the variable last_name to -> the 7th character of name to the 
last character of name.

funky_name = name[::2] | OUTPUT => "JsJeoe"
^^^^^^^^^^^^^^^^^^^^^^
Here we are assigning the variable funky_name to -> the step 2, which will only
count every other character.

reversed_name = name[::-1] | OUTPUT => "edoCeeJtsuJ"
^^^^^^^^^^^^^^^^^^^^^^^^^^
Here we are assigning the variable reversed to -> the step -1, which will count 
every character from end to start.


SLICING:

website1 = "http://google.com" <- Assigning website1 to google's link.

website2 = "http://wikipedia.com" <- Assigning website2 to wikipedia's link.

web_slice = slice(7, -4) <- First number is start and the second number is stop.
^^^^^^^^^
Here we are assigning the variable web_slice to the slice function.

We can use our slice in the index area to grab index 7 to index -4.
Index -4 counts back from the end of the string.

print(website1[web_slice]) | OUTPUT => "google"

print(website2[web_slice]) | OUTPUT => "website"
