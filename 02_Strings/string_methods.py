######## String Methods #######


txt = "Hello, And Welcome To My World!"

# 1
# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

# print(txt.casefold())


#2
# The count() method returns the number of times a specified value appears in the string.
# string.count(value, start, end)
# print(txt.count('Hello'))

#3
# The endswith() method returns True if the string ends with the specified value, otherwise False.
# string.endswith(value, start, end)
# print(txt.endswith('.'))
# print(txt.endswith(" ", 5, 11))

#4
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

# print(txt.find("hello")) # output : -1  #because string not found
# print(txt.find("World"))


