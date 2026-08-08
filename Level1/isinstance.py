# how do the type() and isinstance() function Work?
devloper  = "Prabin"
# we can see what type "devloper" is from the value it has through which type it cantains by using type function..
print(type(devloper))

# output:<class 'str'> means that devloper is string type
my_integer_var = 200
print(type(my_integer_var))

my_float_var = 200.3443
print(type(my_float_var))

my_string_var ='i am missing you python'
print(type(my_string_var))

my_blooean_var = False
print(type(my_blooean_var))

my_set_var = {7,'krishne',9.4999}
print(type(my_set_var))

my_dictionary_var = {'name':'Balaram','age':17}
print(type(my_dictionary_var))

my_none_var = None
print(type(my_none_var))

# now There will be times in your program when you need to verify that a particular variable is a specific type before performing operations on it. 
# this is where the isinstance() function comes in handy.


# account_money = '50000'
# account_money/2
# print(account_money)
#  to see account money is an integer or not we use isinstance()

account_money = '50000'
print(isinstance(account_money, (int, float)))
# isinstance returns True if account_money is an int or float, otherwise it returns False.
print(isinstance(account_money ,str))