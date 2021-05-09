import sys
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\A118090\OneDrive - AXAXL\Desktop\hello_django\Athlete Dataset Analysis\archive (1)\athlete_events.csv")

def nan_percent(df, column_name):
    row_count = df[column_name].shape[0]
    empty_rows = row_count - df[column_name].count()
    return (100.0*empty_rows)/row_count
    vrc
# def NaN_percent(df, column_name):4
#     row_count = df[column_name].shape[0]
#     empty_values = row_count - df[column_name].count()
#     return (100.0*empty_values)/row_count

# print(df.shape)   
print(list(df))

for i in list(df):
     print(i +': ' + str(nan_percent(df,i))+'%')  

unique_athletes = len(df['Name'].unique())
print("Unique athletes:" + str(unique_athletes))

#Replace nan with None
df['Medal'] = df['Medal'].fillna('None')

df1 = df.loc[df['Medal']!='None']
print(df['Medal'].unique())
# Number of athletes winning medals
# medal_winners =len(df.loc[df['Medal']!='None']['Name'].unique())
medal_winners =len(df['Name'].unique())
print("Medal winner athletes:" + str(medal_winners))

#number of medals distrubuted 

medals_distributed = df.loc[df['Medal']!='None']['Medal'].value_counts()
print("Medal distributed: \n" + str(medals_distributed))


team_medal_count = df1.groupby(['Team','Medal'])['Medal'].agg('count')                                  
team_medal_count = team_medal_count.reset_index(name = 'count').sort_values(['count'],ascending=False)
# print(team_medal_count)

unique_men = len(df.loc[df['Sex'] == 'M']['Name'].unique())
unique_women = len(df.loc[df['Sex'] == 'F']['Name'].unique())

print("Total Men and Women participation: ")
print(unique_men,unique_women)                      

men_medals   = df1.loc[df1['Sex'] == 'M']['Medal'].count()
women_medals   = df1.loc[df1['Sex'] == 'F']['Medal'].count()

print("Total Medals won by Men and Women: ")
print(men_medals,women_medals)


f_year_count = df1.loc[df1['Sex'] == 'F'].groupby('Year').agg('count')['Name']
m_year_count = df1.loc[df1['Sex'] == 'M'].groupby('Year').agg('count')['Name']
# print(f_year_count)
# print(f_year_count)

sns.scatterplot(data= f_year_count)
# plt.show()
sns.scatterplot(data= m_year_count)
plt.show()