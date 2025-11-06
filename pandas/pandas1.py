import pandas as pd
# #Create a Series
# s= pd.Series([1,2,3,4,5])
# print("Series :",s)

data1 ={
    'Name':['Subesh','Smith','Rajan','Ritesh','amir'],
    'Age' :['12','23','30','45' ,'20'],
    'City':['denkmark','kathmandu','pokhara','htd','sydne']
}
df = pd.DataFrame(data1)
print('DataFrame\n',df)

# selecting row by index

first_row = df.iloc[0]
print('\n First row:\n',first_row)

#adding new salary column
df['salary'] =[70000,5000,30000,60000,500]
print('dataFrame with salary column :\n',df)