#Creating Dataframe

import pandas as pd
import numpy as np

list1=['Geeks','for','Geeks']
df=pd.DataFrame(list1)
print(df)

Dict={'Name':['Ghanshyam','Naresh','Chetan'],'Age':[23,21,16]}
df=pd.DataFrame(Dict)
print(df)

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
print(df[['Name','Age']])

data=pd.read_csv('nba.csv',index_col='Name')
##first=data.loc['Avery Bradley']
##print(first)
first=data['Age']
print(first)

row4=data.iloc[3]
print(row4)

dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
data=pd.DataFrame(dict)
print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.dropna())

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
df=pd.DataFrame(dict)

for i ,j in df.iterrows():
    print(i,j)
    print()

cloumns=list(df)

for i in cloumns:
    print(df[i][3])
address=['Delhi','Mumbai','Chennai','SURAT']
df['Address']=address
print(df)
print(df.head(2))
df.drop(['degree','score'],axis=1,inplace=True)
print(df)
