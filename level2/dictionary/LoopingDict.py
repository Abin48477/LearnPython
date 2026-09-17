products = {
    'laptop':990,
    'Smartphone':100,
    'tablet':250,
    'headphones':500

}
for price in products.values():
    print(price)

# output
# 990
# 100
# 250
# 500
for item in products.items():
    print(item)
# ('laptop', 990)
# ('Smartphone', 100)
# ('tablet', 250)
# ('headphones', 500)

# iterate over a dictionary which keeping track use enumerate
for index, product in enumerate(products.items()):
    print(index,product)

