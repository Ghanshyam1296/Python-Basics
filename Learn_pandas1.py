#Exploring Pandas

import pandas as pd
import numpy as np

data=pd.read_csv('nba.csv',index_col='Name')
#first=data[['Age','College','Salary']]
first=data.loc['Ed Davis']
print(first)

##second=data.loc[:,['Age','College','Salary']]
##print(second)

row4=data.iloc[[3,4,5]]
print(row4)

t=data.iloc[[1,2],[3,4]]
print(t)

print(data[:10])
print(data.dropna(inplace=True))
print(type(data.Number[0]))

data.Number=data.Number.astype('int64')

print(type(data.Number[0]))

df = pd.DataFrame({"A":["sofia", 5, 8, 11, 100], 
                   "B":[2, 8, 77, 4, 11], 
                   "C":["amy", 11, 4, 6, 9]})

print(df)
print(df.info())
df_new=df[1:]
df_new=df_new.infer_objects()
print(df_new.info())

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[90, 40, 80, 98]}

df1=pd.DataFrame(dict)
##print(df1)

for i,j in df1.iterrows():
    print(i,j)

for key,value in df1.iteritems():
    print(key,value)

for i in df1.itertuples():
    print(i)

data=data.head(3)
for i in data.itertuples():
    print(i)

dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]}
df=pd.DataFrame(dict)
print(df.isnull())
print(df.notnull())
df=df.interpolate(method='linear',limit_direction='backward')
print(df)

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
df['Name']=df['Name'].str.upper()
df['Address']=df['Address'].str.split("a",n=1,expand=True)
print(df)

##data=pd.read_csv('nba.csv',index_col='Name')
##data['Age']=data['Age'].replace(25.0,'Twenty Five')
##filter=data['Age']=='Twenty Five'
##print(data.where(filter).dropna())
new=df['Address'].copy()
df['Name']=df['Name'].str.cat(new,sep=",")
print(df)
s=pd.Series(['a1','b2','c3'])
##s=s.str.extract(r'([ab])(\d)')
s = s.str.extract(r'(?P<Letter>[ab])(?P<Digit>\d)')
print(s)

datedata=pd.date_range('1/1/2011', periods = 10, freq ='H')
print(datedata)
x=pd.datetime.now()
print(x.month,x.year,x.day)

rng=pd.DataFrame()
rng['date']=pd.date_range('1/1/2011',periods=72,freq='H')
rng['year']=rng['date'].dt.year
rng['month']=rng['date'].dt.month
rng['day']=rng['date'].dt.day
rng['hour']=rng['date'].dt.hour
rng['minute']=rng['date'].dt.minute
print(rng.head(3))

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
df=pd.DataFrame(data1,index=[0,1,2,3])
df1=pd.DataFrame(data2,index=[4,5,6,7])

df_concate=[df,df1]
df2=pd.concat(df_concate,axis=1,join_axes=[df.index])
print(df2)

Data=[1,3,4,5,6,7,8,9]
index=['a','b','c','d','e','f','g','i']
si=pd.Series(Data,index)
print(si)

Data=[[2,3,4],[5,6,7]]
snd=pd.Series(Data)
print(snd)

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])            
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3]) 
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])
Data ={'first':s1, 'second':s2, 'third':s3}
dfseries=pd.DataFrame(Data)
print(dfseries)

data = pd.read_csv("employees.csv")
new = data["Gender"] != "Male"
data=data[new].dropna()
print(data)

