"""Simple, step-by-step examples of assert and StopIteration."""


# 1. A real-world assert: validate an order before processing it.
order_total = 25
assert order_total > 0, "The order total must be greater than zero"
print("Order is ready to process")


# 2. StopIteration happens when next() has no more values to return.
steps = iter(["Pack order", "Ship order"])

while True:
	try:
		step = next(steps)
		print(step)
	except StopIteration:
		print("All order steps are complete")
		break


age = -5
# assert age >= 0#The print() doesn't happen because Python stopped at assert.security guard
# print("Age is valid")

assert age >=0,"Age cannot be negative"
# assert
#   ↓
# CHECK condition
#   ↓
# True?  → Continue ✅
# False? → AssertionError ❌

# if + raise → validate user input / normal program errors
# assert → check something you expect should always be true
# Remember this one sentence:

# assert = "Python, make sure this is true. If not, STOP!" 🚨