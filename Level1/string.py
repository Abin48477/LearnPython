# if want to do multiline string,you can use triple double quotes or single quotes:
my_str_3 = """Multiline 
string"""
my_str_4 = '''Another 
multiline 
string'''
print(my_str_3)
print()
print(my_str_4)

# Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:
msg = "it's a sunday today"
print(msg)

quote = 'She said, "Hello World"'
print(quote)

# Escape the single or double quotation mark in the string with a backslash (\). With this method, you can use either single or double quotation marks to wrap the string itself:
msg1 = "you\'r very good gye!"
msg2 = 'she said, \"hello world\"'
print(msg1)
print(msg2)

# use "in" operatior to find whether the character or characters exit in the string or not this return boolean 
my_str = 'hello world'
print('hello' in my_str)

print('H' in my_str)

print('hl' in my_str)

print("wo" in my_str)
print('z' in my_str)

# To get the length of a string, you can use the built-in len() function. Here's an example:
my_str33 = 'hello world'
print(len(my_str))
print(my_str33[0])
print(my_str33[6])
# Negative indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2, and so on:

print(my_str33[-1])
print(my_str33[-2])

