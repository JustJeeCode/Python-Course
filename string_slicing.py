# Slicing = create a substring by extracting elements from another string.
# indexing[] or slice()
# [start:stop:step]

# name = "JustJeeCode"

# first_name = 0 to 7.
# first_name = name[:7]
# last_name = 7 to the end.
# last_name = name[7:]
# funky name is start to end but incremented by 2.
# funky_name = name[::2]
# incremented by -1 so it will be reversed.
# reversed_name = name[::-1]

website1 = "http://google.com"
website2 = "http://wikipedia.com"

# slicing index 7 to -4
web_slice = slice(7, -4)
print(website1[web_slice])
print(website2[web_slice])
