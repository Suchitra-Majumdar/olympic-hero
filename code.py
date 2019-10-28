# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)
#Code starts here
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)



# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event']=np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])
better_event=data['Better_Event'].value_counts().argmax()
#better_event=data['Better_Event'].value_counts().index.values[0]


# --------------
#Code starts here



top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.tail()
top_countries.drop(index=146, axis = 0,inplace=True)
def top_ten(df,cols):
    country_list=[]
    top_10 = df.nlargest(10, cols)
    country_list.extend(top_10['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=list((set(top_10_summer) & set(top_10_winter) & set(top_10)))  


# --------------
#Code starts here




summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

fig, (ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1,figsize=(15,15))
ax_1.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
ax_1.set_title('Top 10 Summer')
ax_2.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
#ax_2.set_title('Top 10 Winter')
ax_3.bar(summer_df['Country_Name'],top_df['Total_Medals'])
ax_3.set_title('Top 10 Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_max_ratio].iloc[0,0]#['Country_Name']
print(str(summer_country_gold))
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df[winter_df['Golden_Ratio']== winter_max_ratio].iloc[0,0]#['Country_Name']
print(str(winter_country_gold))
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio].iloc[0,0]#['Country_Name']
print(str(top_country_gold))
top_max_ratio



# --------------
#Code starts here



data_1=data.drop(index=146,axis=0)
data_1['Total_Points']=3*data_1['Gold_Total']+2*data_1['Silver_Total']+1*data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country=data_1[data_1['Total_Points']==most_points].iloc[0,0]
print(most_points)
print(best_country)


# --------------
#Code starts here




best=data[data['Country_Name']==best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


