import pandas as pd
"""data = {
    'Name': ['Aman', 'Riya', 'Karan', 'Riya', 'Sara'],
    'Age': [20, 22, 19, 21, 23],
    'City': ['Delhi', 'Mumbai', 'delhi', 'Pune', 'Mumbai'],
    'Marks': [-85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)

df_row=df.drop_duplicates(subset=['Name','City'])
print("duplicate rows delete:\n",df_row)

print(df.loc[(df['Marks']>=85) & (df['Age']<22),['Name','Marks']])
print(df.loc[df['Marks']<0,'Marks'])"""

"""Marks =[]
Passed_count=0
Failed_count=0
for i in range(5):
    numbers=int(input("enter the marks: "))
    Marks.append(numbers)
for num in Marks:
    if num >= 40:
            print(f"passed student marks:{num}")
            Passed_count +=1
    else:
            print(f"failed student marks: {num}")
            Failed_count +=1
print(f"total passed:{Passed_count}")
print(f"total Failed:{Failed_count}")"""
""" import numpy as np
data = {
    'Name': ['Aman', 'Riya', 'Karan', 'Riya', 'Sara'],
    'City': ['Delhi', 'Mumbai', np.nan, 'Mumbai', 'Pune'],
    'Marks': [-85, 90, 78, 90, 88]
}
df = pd.DataFrame(data)
df['City']=df['City'].fillna('unknown')
print("filling the missing value in city:\n",df)
print(df.drop_duplicates())
print(df['Marks'].unique())"""
# Grocery Project
"""GroceryItems=[]
Prices=[]
total_bill=0
for i in range(5):
    item=input("Enter the Grocery Name: ")
    price=int(input("enter the price: "))
    GroceryItems.append(item)
    Prices.append(price)

for p in Prices:
    if p >= 50:
       print(p," is more than 50")
    else:
        print(p, "is less then 50")
    total_bill+=p
print("Total bill:",total_bill)"""
#Count of maximum employee salary more than 50000
Salary=[25000, 48000, 52000, 61000, 75000, 30000]
Salary_count=0
for s in Salary:
    if s >= 50000:
        Salary_count+=1
print (f"count of maximum Salary", Salary_count)

data = {
    'Name': ['Aman', 'Riya', 'Karan', 'Meena', 'Sara'],
    'Department':['HR','IT','Sales','HR','IT'],
    'Age': [25, 28,35,30,27],
    'Salary':[40000,55000,60000,-45000,70000]
}
df = pd.DataFrame(data)
print(df[df['Salary']>50000])
df_row=df.drop_duplicates()
print("delete duplicate rows:\n",df_row)
df['Salary']=df['Salary'].abs()
print(df)





     




        






    
        

        



    