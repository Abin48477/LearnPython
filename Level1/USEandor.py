age = 20
if age>= 18 and age <=60:
    print("Allowed")

# age >= 18  → True ✅
# age <= 60  → True ✅

# True AND True → True ✅
# 1. and = BOTH must be true

# or = ANY ONE can be true
age = 70

if age < 18 or age > 60:
    print("Special case")

# age < 18  → False ❌
# age > 60  → True ✅

# False OR True → True ✅