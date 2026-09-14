# re is a built in module used for Regular Expressions(regex)
import re

text = "My age is 25"
result = re.search(r"\d+",text)
print(result)

# \d+ --> one or more digits(0-9)
# real life exampel
import re

email = "john@gmail.com"

if re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
    print("Valid email")
else:
    print("Invalid email")
# | Function       | Purpose                         |
# | -------------- | ------------------------------- |
# | `re.search()`  | Find a pattern anywhere in text |
# | `re.match()`   | Check pattern at the beginning  |
# | `re.findall()` | Find all matches                |
# | `re.sub()`     | Replace matching text           |
# | `re.split()`   | Split text using a pattern      |
