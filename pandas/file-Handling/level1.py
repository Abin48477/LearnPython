# 1st
# file = open ("new_file.txt",'w')
# file.write('This is line 1.\n')
# file.write('This is line 2.\n')
# # file.close()


# 2nd
# lines=['Lumbini\n','ICT\n','Campus\n']
# file = open('new_file.txt','w')
# file.writelines(lines)
# file.close()

# 3rd
# file =open('new_file.txt','r')
# content = file.read()
# print(content)
# file.close()

# 4th
# file = open("new_file.txt",'r')
# line1 = file.readline()
# line2 = file.readline()

# print("line 1:",line1)
# print("line 2:",line2)

# file.close()

# 5th
file = open ('new_file.txt','r+')
content= file.read()
print("current content:")
print(content)

# Append new content
file.write('Appending new content\n')
file.write('Updated content.')
file.seek(0)
content=file.read()
print('Updated content.')
print(content)
file.close()
