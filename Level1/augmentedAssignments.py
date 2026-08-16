#  variable <operator>= value is better then this

#  variable = variable <operator> value
my_var = 10
my_var +=5

print(my_var)

my_var1 = 20
my_var1 -=10 #(my_var1 = my_var1+10)
print(my_var1)

my_string = 'hare'
my_string += 'krishna'
print(my_string)

# to make multiple of string we use *=
my_string1 = 'rama'
my_string1 *= 5
print(my_string1)

# incremant and decrement operators ++ or -- is not used in python
# simply saying x += 1 is increment and x -= 1 is decrement 
var = 5
print(+var)#5
print(++var)#5 python look like +(+var) Since +var simply means positive var, nothing changes.
print(+++var) #5

var += 1 #increase by 1
print(var) #6

# Unary: -x → one value
# Binary: x + y → two values