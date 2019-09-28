# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here
df = pd.read_csv(path)
X = df.drop(['customerID','Churn'],1)
y = df['Churn']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)




# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here
X_train['TotalCharges'] = X_train['TotalCharges'].replace(' ',np.NaN)
X_test['TotalCharges'] = X_test['TotalCharges'].replace(' ',np.NaN)
X_train['TotalCharges'] = X_train['TotalCharges'].astype(float)
X_test['TotalCharges'] = X_test['TotalCharges'].astype(float)
X_train['TotalCharges'] = X_train['TotalCharges'].fillna( X_train['TotalCharges'].mean())
X_test['TotalCharges'] = X_test['TotalCharges'].fillna( X_test['TotalCharges'].mean())
print(X_train['TotalCharges'].isnull().sum())
print(X_test['TotalCharges'].isnull().sum())

le = LabelEncoder()
cols = list(X_train.select_dtypes(exclude=['int64','float64']).columns) 
print(cols)
X_train[cols] = X_train[cols].apply(lambda col : le.fit_transform(col))
X_test[cols] = X_test[cols].apply(lambda col : le.fit_transform(col))
# X_train = le.fit_transform(X_train)
# X_test= le.transform(X_test)
y_train = y_train.replace({'No':0, 'Yes':1})
y_test = y_test.replace({'No':0, 'Yes':1})


# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
print(X_train.head())
print(X_test.head())
print(y_train.head())
print(y_test.head())
ada_model = AdaBoostClassifier(random_state=0)
ada_model.fit(X_train,y_train)
y_pred = ada_model.predict(X_test)
ada_score = accuracy_score(y_pred,y_test)
ada_cm = confusion_matrix(y_pred,y_test)
ada_cr = classification_report(y_pred,y_test)
print(ada_score)
print(ada_cm)
print(ada_cr)


# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_model = XGBClassifier(random_state=0)
xgb_model.fit(X_train,y_train)
y_pred = xgb_model.predict(X_test)
xgb_score = accuracy_score(y_pred,y_test)
xgb_cm = confusion_matrix(y_pred,y_test)
xgb_cr = classification_report(y_pred,y_test)
print(xgb_score)
print(xgb_cm)
print(xgb_cr)

clf_model = GridSearchCV(estimator=xgb_model,param_grid=parameters)
clf_model.fit(X_train,y_train)
y_pred = clf_model.predict(X_test)
clf_score = accuracy_score(y_pred,y_test)
clf_cm = confusion_matrix(y_pred,y_test)
clf_cr = classification_report(y_pred,y_test)
print(clf_score)
print(clf_cm)
print(clf_cr)





