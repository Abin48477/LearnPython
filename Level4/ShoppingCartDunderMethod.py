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

    def __getitem__(self, index):
        return self.items[index]
    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)
cart = Cart()
cart.add('Laptop')
cart.add("mouse")
cart.add("charger")
cart.add("mobile")
cart.add("keyboard")
cart.remove("mobile")

print(cart.list_items())#['Laptop', 'mouse', 'charger', 'keyboard']
print(cart.__getitem__(1)) #mouse
print(len(cart)) #1
print("Laptop" in cart) #True
print(cart.__iter__())
