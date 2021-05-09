import sys
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\A118090\OneDrive - AXAXL\Desktop\hello_django\Athlete Dataset Analysis\archive (1)\athlete_events.csv")

# print(df.isnull().sum())

print(list(df))
print(type(df))

# for i in list(df):
#     print(i)
    
print(df['Age'].shape[0])
print(df['Age'].count())

print(df['ID'].shape[0])
print(df['ID'].count())

print(len(df['ID'].unique()))
print(len(df['Name'].unique()))

print(df['Medal'].shape[0])
print(df['Medal'].unique())

df['Medal'] = df['Medal'].fillna('heena')

print(df['Medal'].unique())

print("number of athletes")
print(len(df['Name'].unique()))


print("number of medal winner athletes")
print(len(df.loc[df['Medal'] !='heena']['Name'].unique()))

df1 = df[['Name','Medal']]

df1_gb = df1.groupby(['Medal']).count()
print(df1_gb)
df2 = df.loc[df['Medal'] !='heena']


males = df.loc[df['Sex'] == 'M']['Name'].unique()

females = df.loc[df['Sex'] == 'F']['Name'].unique()

print(len(males))
print(len(females))

medals_men = df[df['Sex'] == 'M']

medals_men1 = medals_men[medals_men['Medal']!= 'heena'].count()

print(medals_men1)

plotpoints = df.loc[df['Sex'] == 'M'].groupby('Year').agg('count')['Name']

print(type(plotpoints))
sns.scatterplot(data = plotpoints)
plt.show()

medals_in_year = df.groupby('Medal').agg('count')['Name']

medals_in_year.plot.bar(rot=15, title="Plot");

plt.show(block=True);
