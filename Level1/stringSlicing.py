# Syntax
# string[start:stop]
my_str = "hello world"
print(my_str[1:4])# ell 
# Note that the stop index is non-inclusive, so [1:4] just extracted the characters from index 1, and up to, but not including, the character at index 4.

print(my_str[:7])
# This extracts everything from index 0 up to (but not including), the character at index 7. And here's what happens if you omit the stop index:

print(my_str[8:])
# this extracts everything from the character at index 8 until the end of the string.

print(my_str)
# Note that slicing a string does not modify the original string:

print(my_str[:])

# step parameter
# string[start:stop:step]
# In the example below, the slicing starts at index 0, stops before 11, and extracts every second character:
my_str1 = "hello world"
print(my_str[0:11:2])#hlowrd

# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank:
print(my_str1[::-1])