import pandas as pd
# #Create a Series
# s= pd.Series([1,2,3,4,5])
# print("Series :",s)

# data1 ={
#     'Name':['Subesh','Smith','Rajan','Ritesh','amir'],
#     'Age' :[12,23,30,45 ,20],
#     'City':['denkmark','kathmandu','pokhara','htd','sydne']
# }
# df = pd.DataFrame(data1)
# print('DataFrame\n',df)

# # selecting row by index

# first_row = df.iloc[0]
# print('\n First row:\n',first_row)

# #adding new salary column
# df['salary'] =[70000,5000,30000,60000,500]
# print('dataFrame with salary column :\n',df)


# #Filtering Data:Show the data  Whose age > 25
# filter_data = df[df["Age"] > 25]
# print("\n Filtered Data:",filter_data)

# #using head to view first 3rows

# print('\n First 3 rows of df \n ',df.head(3))

# #using  tail
# print("\n last 3 rows of df :",df.tail(3))

# #accessing DataFrame attributes
# print('\n DataFrame Index:\n ',df.index)
# print('\n DataFrame Columns:\n ',df.columns)
# print('\n DataFrame Data Types:\n ',df.dtypes)
# print('\n DataFrame Shape:\n ',df.shape)
# print('\n DataFrame Size:\n ',df.size)
# print('\n DataFrame Values:\n ',df.values)
# print('\n DataFrame Transpose:\n ',df.T)
# print('\n DataFrame Info:\n ',df.info())

# #for Series
# ser=pd.Series([1,2,3],index=['a','b','c'],name = "Example Series")


# data ={
#     "Name":["susasan","abin","rajan","manita","amrita"],
#     "Age":[25,32,32,12,4],
#     "City":["Bus-park",None,'Ksheraprur',"parsa",'parbatipur']
# }
# df = pd.DataFrame(data)
# print("Is Null: \n",df.isnull())
# df_dropped_rows = df.dropna()
# print("DataFRame with dropped rows:\n",df_dropped_rows)

# df_dropped_columns = df.dropna(axis = 1)
# print("DataFrame with dropped columns:\n",df_dropped_columns)

# #filling
# df_filled_ffill = df.fillna(method ="ffill")
# print("DataRaame with forward filll\n",dr_filled_ffill)

# df_filled_ffill = df.fillna(method="ffill")
# print("DataFrame with backward fill:\n",df_filled_bfill)

# #Selecting rows where city is "Parsa"

# city = df[df["City"]=="Parsa"]

# print("\n Rows where city is Para\n",city)

# df = pd.DataFrame(data)
#save the dataframe to csv file
data ={
    "Name":["susasan","abin","rajan","manita","amrita"],
    "Age":[25,32,32,12,4],
    "City":["Bus-park",'gaidakot','Ksheraprur',"parsa",'parbatipur']
}
df = pd.DataFrame(data)
df.to_csv('example.csv',index=False)
print("\n Dataframe saved successfully!")

#now after adding rows and columns named 'Salaries'
#Read the csv file
df= pd.read_csv('example.csv')
#show basic information
print("DataFrame Info:")
print(df.info())

#show the mean of the age
age_mean =df["Age"].mean()
print("Mean of Age:",age_mean)


#Filter dataframe for rows where age>25 then save the record as filerdata.csv

filter = df[df['Age']>25]
print("Age>25:\n",filter)
filter.to_csv ('filterdata.csv',index=False)
