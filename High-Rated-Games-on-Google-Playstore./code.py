# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
# ratings = data['Rating'].value_counts()
data.hist('Rating')
# print(ratings)
data = data[data['Rating']<=5.0]
# ratings = data['Rating'].value_counts()
data.hist('Rating')
#Code ends here


# --------------
# code starts here
total_null = pd.Series(data.isnull().sum())
percent_null = pd.Series(total_null/data.isnull().count())
missing_data = pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)
data.dropna(inplace=True)
total_null_1 = pd.Series(data.isnull().sum())
percent_null_1 = pd.Series(total_null_1/data.isnull().count())
missing_data_1 = pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)
# code ends here


# --------------

#Code starts here
plot = sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)
plot.set_xticklabels(rotation=90)
# sns.suptitle('Rating vs Category [BoxPlot]')
fig = plot.fig 

fig.suptitle('Rating vs Category [BoxPlot]', fontsize=12)

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())

data['Installs'] = data['Installs'].str.replace(',', '')
data['Installs']= data['Installs'].str.replace('+', '')
data['Installs']= data['Installs'].astype(int)
print(data['Installs'])

le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
plot = sns.regplot(x="Installs", y="Rating",data=data)


plt.title('Rating vs Installs [RegPlot]', fontsize=12)

#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())

data['Price'] = data['Price'].str.replace('$','')
data['Price']= data['Price'].astype(float)

sns.regplot(x="Price", y="Rating",data=data)
plt.title('Rating vs Price [RegPlot]')
#Code ends here


# --------------

#Code starts here
print(data['Genres'].unique())

new = data['Genres'].str.split(";",n = 1, expand = True)
# print(new)
data['Genres'] = new[0]
# print(data.columns)
d = data.loc[:,['Rating','Genres']]
gr_mean = d.groupby(['Genres'],as_index=False).mean()
print(gr_mean.describe())
gr_mean = gr_mean.sort_values(['Rating'])
print(gr_mean['Rating'].iloc[0])
print(gr_mean['Rating'].iloc[-1])
# print(gr_mean[-1])
#Code ends here


# --------------

#Code starts here
import datetime 
print(data['Last Updated'])
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()
print(max_date)
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
print(data['Last Updated Days'])
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
#Code ends here


