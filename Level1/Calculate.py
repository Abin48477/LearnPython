my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float2 // my_float_1
print(floor_div_ints)
print(floor_div_floats)

# 56 // 12

# First do normal division:

# 56 ÷ 12 = 4.6666...

# Now floor means take the number and go down to the nearest whole number:
# ⭐ Easy rule to remember

# / → normal division

# // → division + round DOWN (floor)
# One important detail: floor means toward negative infinity, not simply “remove decimals.” For example:

# -10 // 3

# gives -4, because -3.333... rounded down is -4.
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089


# round()
print(round(4.798))#5


print(round(4.253,1))#4.3
# here 1 meands keep 1 digit after decimal

#abs()
# gives the positive value 
print(abs(-2433342))

print(pow(2,3))#gives 8
print(2**3)#gives 8
print(2,3,8) #means (2³) % 5