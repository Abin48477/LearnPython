class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money!")

    return balance - amount

print(withdraw(100,150))