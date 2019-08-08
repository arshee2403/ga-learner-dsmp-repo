# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here


# read the dataset
dataset = pd.read_csv(path)


# look at the first five columns
print(dataset.head(5))

# Check if there's any column which is not useful and remove it like the column id
print(dataset.isnull().sum())
dataset.drop('Id',axis=1,inplace=True)
# check the statistical description
print(dataset.describe())
print(dataset.info())



# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols = list(dataset.columns)

#number of attributes (exclude target)
size = len(cols)

#x-axis has target attribute to distinguish between classes
x = dataset['Cover_Type']


#y-axis shows values of an attribute
y = dataset.drop('Cover_Type',axis=1)

#Plot violin for all attributes
# fig, ax = plt.subplots(figsize =(9, 7)) 

# sns.violinplot(x=x , y = y['Aspect'] ) 

fig,axes = plt.subplots(nrows = 6 , ncols = 5,figsize =(10, 7))
for i in range(6):
    for j in range(5):
        col=cols[ i * 2 + j]
        sns.violinplot(x=x, y=dataset[col], ax=axes[i,j])


# --------------
import numpy
upper_threshold = 0.5
lower_threshold = -0.5


# Code Starts Here
subset_train = dataset.iloc[:,0:10]
data_corr = subset_train.corr()
sns.heatmap(data_corr)
correlation = data_corr.unstack().sort_values(kind='quicksort')
corr_var=[]
corr_var.append(correlation[correlation>upper_threshold])
corr_var.append(correlation[correlation<lower_threshold])
# print(correlation.iloc[0::])
corr_var_list=[]
# for i in range(0,len(corr_var_list)):
#     corr_var_list.append(corr_var_list[i])
# print(corr_var_list)
for i in range(0,correlation.shape[0]):
    if ((correlation[i]>upper_threshold) or (correlation[i]<lower_threshold)) :
        if (correlation[i]!=float(1)):
            corr_var_list.append(correlation[i])
print(corr_var_list)

# Code ends here




# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)
Y = dataset['Cover_Type']

X = dataset.drop('Cover_Type',axis=1)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.
scaler = StandardScaler()
X_train_temp = scaler.fit_transform(X_train)
X_test_temp = scaler.transform(X_test)
# X_train_1= pd.DataFrame(X_train_temp)
# X_test_1= pd.DataFrame(X_test_temp)
# X_train1 = pd.concat([X_train_temp,X_train],axis=1)
# X_test1 = pd.concat([X_test_temp,X_test],axis=1)

scaled_features_train_df = pd.DataFrame(X_train_temp,index=X_train.index,columns=X_train.columns)
print(scaled_features_train_df)
scaled_features_test_df = pd.DataFrame(X_test_temp,index=X_test.index,columns=X_test.columns)
print(scaled_features_test_df)
#Standardized
#Apply transform only for continuous data


#Concatenate scaled continuous data and categorical



# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:
print(scaled_features_train_df.shape)
print(Y_train.shape)
skb = SelectPercentile(score_func=f_classif,percentile=20)
predictors = skb.fit_transform(scaled_features_train_df,Y_train)
scores = list(skb.scores_)
Features = scaled_features_train_df.columns
data = {'Features':Features,'scores':scores}
dataframe = pd.DataFrame(data).sort_values("scores",ascending=False)
# print(dataframe)
top_k_predictors = list(dataframe['Features'].iloc[0:11])
print(top_k_predictors)





# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score

clf = OneVsRestClassifier(LogisticRegression())
clf1 = OneVsRestClassifier(LogisticRegression())
model_fit_all_features = clf1.fit(X_train,Y_train)
predictions_all_features = clf1.predict(X_test)
score_all_features = accuracy_score(Y_test,predictions_all_features)

model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors],Y_train)
predictions_top_features = clf.predict(scaled_features_test_df[top_k_predictors])
score_top_features = accuracy_score(Y_test,predictions_top_features)

print(score_all_features)
print(score_top_features)




