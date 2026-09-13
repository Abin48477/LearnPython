# sometimes the module name is long so we give nickname called Alias---as

import math as m
# import class
import datetime
# if u dont want the whole toolbox import only the necessary items
from math import radians,sin ,cos,pow as p


angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value)
print(cos_value)

print(m.sqrt(36))#6.0
print(pow(5,2))#25.0 here i dont need to use math or m using from i can do directly 
print(p(2,2))#4.0

# from math import * this create name collision same name so it create confusion
# importing  a constant
print(m.pi)
# importing a class
birthday = datetime.date(2003,1,10)
# here date is a class


# if __name__ == "__main__":
# "If this file is being run directly, then do the following."
# if __name__ == "__main__": is used to make sure certain code runs only when the Python file is executed directly, and not when the file is imported as a module.