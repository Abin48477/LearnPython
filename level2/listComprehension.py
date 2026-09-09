even_numbers = [num for num in range(21) if num%2 ==0]
print(even_numbers)

numbers = [1,2,3,4,5]
result =[(num, 'Even') if  num%2 ==0 else (num,'Odd') for num in numbers]
print(result)

# real world example
prices = [1000,1000,200,50,500]
result=[price for price in prices if price>100 ]

print(result)

# [WHAT_I_WANT for ITEM in LIST if CONDITION]
# ask 3 questions
# what do i want to put in the new list?price
# [num * 2 for num in numbers] here num*2 is important becase what result i want 
# Where am i getting the items from?for price in prices
# Which items do i want?if price > 100