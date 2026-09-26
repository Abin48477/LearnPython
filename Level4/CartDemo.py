class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self,  index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart() # make object
cart.add('Laptop') 
cart.add("Wireless mouse")
cart.add("Ergo keyboard")
cart.add("monitor")

for item in cart:
    print(item, end = " ")

print(len(cart))
print(cart[3])

print('Monitor' in cart)
print("banana" in cart)

cart.remove('Ergo keyboard')

print(cart.list_items())

cart.remove('banana') # banana is  not in cart