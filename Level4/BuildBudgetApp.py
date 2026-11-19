class Category:
    def __init__(self,name):

        self.name = name
        self.ledger = []

    def deposit(self,amount, description=""):
  
        self.ledger.append({
            "amount":amount,
            "description": description
        })
    def withdraw(self,amount,description=""):

        self.ledger.append({
            "amount":-amount,
            "description":description
        })
        return True #Tells us that the withdrawal succeeded.
    
    def get_balance(self):
       
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total
    
    # Python compares two values:
# - amount: How much we want to withdraw.
# - self.get_balance(): How much money we currently have.
    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

            
food = Category("food")
clothing  = Category("Clothing")

food.deposit(1000,"Initial deposit")
food.deposit(200,"Extra money")
food.deposit(50)

food.withdraw(300,"Groceries")
food.withdraw(20,"govindas momo")


print(food.name)
print(clothing.name)
print(food.ledger)
print(clothing.ledger)

print(food.get_balance())

print(food.check_funds(20000))
print(food.check_funds(10))


