# pause the program
import pdb

def divide(a,b):
    pdb.set_trace()  # 🛑 STOP HERE
    return a/b
print(divide(10,2))

# pdb.set_trace()
# it basically says:
# stop!Lets investigate here.

# output
# -> return a/b
# (Pdb) p a
# 10
# (Pdb) p b
# 2
# (Pdb) c
# 5.0
# --Return--
# here 'c' meaning continue and 'p' meaning print
