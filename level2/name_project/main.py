import calculator
print("Main file is running")
print(calculator.add(200,20))
# output:
# calculator file is running.
# 13
# 6
# Main file is running
# 220
# here the output from calculator.py also printed which we dont wanted only function should work so we do  if __name__ == "__main__": 
# the present output is only this:
# output:
# Main file is running
# 220