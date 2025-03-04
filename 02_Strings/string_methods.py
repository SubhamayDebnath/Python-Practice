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
# string.find(value, start, end)
# print(txt.find("hello")) # output : -1  #because string not found
# print(txt.find("World"))

#5
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.
# string.index(value, start, end)
# print(txt.index('World'))

#6
# The isascii() method returns True if all the characters are ascii characters  (a-z).
# print(txt.isascii())

#7
#The isalpha() method returns True if all the characters are alphabet letters (a-z).
# print(txt.isalpha())
# print('hello'.isalpha())

#8
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# print(txt.isalnum())
# print('hello1'.isalnum())

#8

