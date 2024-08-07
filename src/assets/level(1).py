# -*- coding: utf-8 -*-
"""level(1).ipynb
 
Author :Ahamed Thaiyub A
Original file is located at
    https://colab.research.google.com/drive/11eMCXdb4TEenpQyid8O14bqLZXdJ4U5n
"""

from google.colab import drive
drive.mount('/content/drive')

pip install scikit-learn-intelex


"""INTSLLATION OF REQUIREMENTS :

## PROBLEM STATEMENT
Employee attrition is a significant issue for companies, resulting in substantial costs for hiring, retraining, productivity, and work loss for each employee who leaves. To address this, a model needs to be built to predict whether an employee is likely to quit in the near future.

# Reading the data sets & knowing about each attribute.
"""

##importing libraries
import pandas as pd
import numpy as np

##reading train_data 
#Reading train_data 
train_attrition = pd.read_csv("/content/drive/My Drive/train_attrition.csv")
train_work = pd.read_csv("/content/drive/My Drive/train_work.csv")

#Reading the employee_data
emp_data = pd.read_csv("/content/drive/My Drive/employee_data.csv")

#Reading the test data 
test_attrition = pd.read_csv("/content/drive/My Drive/test_attrition.csv")
test_work = pd.read_csv("/content/drive/My Drive/test_work.csv")

"""##viewing train_work

"""

train_work.head()

"""## viewing of all datasets


"""

##viewing train attrition
train_attrition.head()




emp_data.head()

##dimensions 

print("The train_attrition has {} rows & {} columns." .format(train_attrition.shape[0], train_attrition.shape[1]))
print("The train_work has {} rows & {} columns." .format(train_work.shape[0], train_work.shape[1]))

print("The employee data has {} rows & {} columns." .format(emp_data.shape[0], emp_data.shape[1]))

train_work.head()

train_attrition.head()



train_emp_data = pd.merge(train_attrition, emp_data, how='left', on='EmployeeID')

train_emp_data.shape

train_emp_data.head()

train_final = pd.merge(train_emp_data, train_work, on='EmployeeID', how='left')

train_final.shape

train_final.head()

train = train_final.groupby('EmployeeID').agg('max')
train

print("The train_attrition has {} rows & {} columns." .format(train_attrition.shape[0], train_attrition.shape[1]))
print("The train_work has {} rows & {} columns." .format(train_work.shape[0], train_work.shape[1]))

emp_data.head()

print("The employee data has {} rows & {} columns." .format(emp_data.shape[0], emp_data.shape[1]))

test_attrition.head()

"""## Merging the datasets based on the employee data.

## Merging the train data into a single datafrfame
"""


train_emp_data = pd.merge(train_attrition, emp_data, how='left', on='EmployeeID')

train_emp_data.shape

train_final = pd.merge(train_emp_data, train_work, on='EmployeeID', how='left')

print(train_final.shape)
train_final.head()

train = train_final.groupby('EmployeeID').agg('max')

train.head()

"""## Merging the test data into Single data frame. 

"""

test_emp_data = pd.merge(test_attrition, emp_data, how='left', on='EmployeeID')

test_emp_data.head()

test_final = pd.merge(test_emp_data,test_work, how='left', on='EmployeeID')

test_final.head()

test = test_final.groupby(by='EmployeeID').agg('max')

test.shape

train.to_csv("train.csv", index=True)
test.to_csv("test.csv", index=True)

"""## Feature engineering:"""

train_final = pd.read_csv("/content/train.csv")
test_final = pd.read_csv("/content/test.csv")

print((train_final.columns))

print(test_final.columns)

#Dropping
train_final.drop(columns=['EmployeeID'], axis=1,inplace=True)
test_final.drop(columns=['EmployeeID','Left_Company'], axis=1, inplace=True)

print("Train data shape : {} " .format(train_final.shape))
print("Test data shape: {} ".format(test_final.shape))

train_final.head()

# Splitting the Joini_date column into Joini year & Joiing month.

train_final[['joining_year','joining_month']] = train_final['Joining_Date'].str.split("_", expand=True)


test_final[['joining_year','joining_month']] = test_final['Joining_Date'].str.split("_", expand=True)

#checking
train_final.head()

train_final['job_count'] = train_final['Job_History'].str.split(',').str.len()

test_final['job_count'] = test_final['Job_History'].str.split(',').str.len()

#drop

train_final.drop(columns=['Joining_Date'], axis=1, inplace=True)


test_final.drop(columns=['Joining_Date'], axis=1, inplace=True)

train_final.head()

train_final.dtypes #check

test_final.dtypes #check

train_copy = train_final.copy()
test_copy = test_final.copy()

for col in ['TotalWorkingHours','Billable_Hours','Hours_off_Duty','Touring_Hours']:
  train_final[col] = train_final[col].astype('float')

for col in ['TotalWorkingHours','Billable_Hours','Hours_off_Duty','Touring_Hours']:
  test_final[col] = test_final[col].astype('float')



"""### Converting objects to categories """

for col in ['Sex','Designation','NoOfProjects','joining_year','joining_month','Job_History']:
  train_final[col] = train_final[col].astype('category')
#on testing data 

for col in ['Sex','Designation','NoOfProjects','joining_year','joining_month','Job_History']:
  test_final[col] = test_final[col].astype('category')

train_final['Left_Company'] = train_final['Left_Company'].astype('category')

cat_attr = list(train_final.select_dtypes("category").columns) #exclude target column inthe list
num_attr = list(test_final.columns.difference(cat_attr))

# cat_attr.pop()

cat_attr.remove('Left_Company')

cat_attr

num_attr



"""### Columns with missing values"""

missing_cols_train = train_final.columns[train_final.isnull().any()]
print(missing_cols_train)

missing_cols_test = test_final.columns[test_final.isnull().any()]
print(missing_cols_test)

pip install optuna

from sklearnex import patch_sklearn
patch_sklearn()
from IPython.display import HTML
from timeit import default_timer as timer
from sklearnex import patch_sklearn
# The names match scikit-learn estimators
patch_sklearn("SVC")
from sklearnex import patch_sklearn
# The names match scikit-learn estimators
patch_sklearn(["SVC", "DBSCAN","Kmeans"])
from sklearn.ensemble import StackingRegressor
import optuna 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc

def objective(trial):
    params ={
        'C': trial.suggest_float('C', 0.000000001, 1.0),
        'random_state': 0,
        'n_jobs': -1,
    }
    model = LogisticRegression(**params).fit(x_train, y_train)
    y_pred = model.predict_proba(x_val)[:, 1]
    fpr, tpr, _ = roc_curve(y_val, y_pred)
    score = auc(fpr, tpr)
    return score



study = optuna.create_study(sampler=optuna.samplers.TPESampler(seed=123),
                            direction="maximize",
                            pruner=optuna.pruners.HyperbandPruner())



# from sklearn.linear_model import LogisticRegression

# params = {
#     'C': 0.1,
#     'solver': 'lbfgs',
#     'multi_class': 'multinomial',
#     'n_jobs': -1,
# }
# start = timer()
# classifier = LogisticRegression(**params).fit(x_train, y_train)
# train_patched = timer() - start
# f"Intel® extension for Scikit-learn time: {train_patched:.2f} s"

from sklearn import preprocessing
from sklearn.impute import SimpleImputer

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


import warnings
warnings.filterwarnings('ignore')

"""## Dummification"""

y= train_final['Left_Company']

del train_final['Left_Company']
X = train_final

#One hot encoding  train

dummy_train = pd.get_dummies(data= X, columns= cat_attr, drop_first=True)

dummy_train.shape

#One hot encoding in test

test_final = pd.get_dummies(data= test_final, columns= cat_attr, drop_first=True)

print(test_final.shape)

# Aligninng 

dummy_train, test_final = dummy_train.align(test_final, join='left', axis=1)

#checking for missing valurd;
print(test_final.isnull().sum().sum())

test_final.fillna(value=0, inplace=True)




#standardize 

std = StandardScaler() #Instantiating an object. 
std.fit(dummy_train) #Fittin gon th train data

std_x = std.transform(dummy_train) 
std_test = std.transform(test_final)

print(std_x.shape)
print(std_test.shape)

#### now predicting the model ny logisticc regression , desion treee  on 6 - yet to complete level 1



"""# Models On complete std data without splitting : 

 
"""

log_reg = LogisticRegression()

log_reg.fit(std_x, y)

log_pred = log_reg.predict(std_x)

print(f1_score(y, log_pred))



"""##  Model-2  Decision tree :"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# clf_dt =  DecisionTreeClassifier()
# 
# dt_param_grid = {'criterion': ['entropy', 'gini'], 
#                  'max_depth': [3,4,5],
#                  "min_samples_split": [2,5],
#                  "min_samples_leaf": [1,3,5]}
# 
# dt_grid = GridSearchCV(clf_dt, param_grid=dt_param_grid, n_jobs=-1, cv=10,return_train_score=True)
# 
# dt_grid.fit(std_x,y)
# 
# print(dt_grid.best_params_)
# 
# dt_pred = dt_grid.predict(std_x)
# 
# print(f1_score(y, dt_pred))



"""## Model-3 --Build Gradient Boosting """

# Commented out IPython magic to ensure Python compatibility.
# 
# %%time
# clf_gbc = GradientBoostingClassifier()
# 
# gbm_param_grid = {'max_depth': [2,3,4],
#                   'subsample': [0.8,0.6],
#                   'max_features':[0.3], 
#                   'n_estimators': [10, 20, 30],
#                   'learning_rate':[0.1]}
# 
# gbm_grid = GridSearchCV(clf_gbc, param_grid=gbm_param_grid, n_jobs =-1, cv=5)
# 
# gbm_grid.fit(std_x,y)
# 
# print("The Best parameters are: {} .".format(gbm_grid.best_params_))
# 
# train_pred_gb = gbm_grid.predict(std_x)
# 
# print(f1_score(y, train_pred_gb))
# 
#

# Building model after outholding the dataset.

x_train, x_test, y_train, y_test = train_test_split(std_x, y, test_size=0.3, random_state=11, stratify=y)

import pandas as pd
import time
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn import neural_network 
from sklearn import tree
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state=2)

x_train_re, y_train_re = sm.fit_resample(x_train, y_train.ravel())
x_test_re, y_test_re = sm.fit_resample(x_test,y_test.ravel())

"""## Model-1 Gradient Boosting : """

# Commented out IPython magic to ensure Python compatibility.
# 
# %%time
# clf_gbc = GradientBoostingClassifier()
# 
# gbm_param_grid = {'max_depth': [2,3,4],
#                   'subsample': [0.8,0.6],
#                   'max_features':[0.3, 0.4], 
#                   'n_estimators': [1,2,3,4,5,6,7,8,9,10],
#                   'learning_rate':[0.1, 0.01, 0.001]} #making learning rate lesser gave the best results
# 
# gbm_grid_1 = GridSearchCV(clf_gbc, param_grid=gbm_param_grid, n_jobs =-1, cv=5)
# 
# gbm_grid_1.fit(x_train_re,y_train_re)
# 
# print("The Best parameters are: {} .".format(gbm_grid_1.best_params_))
# 
# train_pred_gb_2 = gbm_grid_1.predict(x_train_re)
# test_pred_gb_2 = gbm_grid_1.predict(x_test_re)
# print(f1_score(y_train_re, train_pred_gb_2)*100)
# print(f1_score(y_test_re, test_pred_gb_2)*100)
# 
#



x_train, x_test, y_train, y_test = train_test_split(std_x, y, test_size=0.3, random_state=11, stratify=y)





"""## Model-2  Logit Model :  

"""

log_reg_2 = LogisticRegression()

log_reg_2.fit(x_train_re,y_train_re)

log_reg_pred_train = log_reg_2.predict(x_train_re)
log_reg_pred_test = log_reg_2.predict(x_test_re)

print(f1_score(y_train_re, log_reg_pred_train))
print(f1_score(y_test_re, log_reg_pred_test))

#prediction on test data



"""## Model-3 xgBoost : """

# Commented out IPython magic to ensure Python compatibility.
# 
# %%time
# import xgboost as xgb
# from sklearn.model_selection import GridSearchCV
# xgb = xgb.XGBClassifier()
# 
# 
# kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=143)
# 
# param_grid = {"n_estimators" : [10,15],
#               "max_depth" : [3,5,6,7],
#               "colsample_bytree":[0.7,.8],
#               "learning_rate": [0.001,0.01,0.1],
#               "subsample":[0.8,0.6]}
# 
# xg_grid = GridSearchCV(xgb, param_grid=param_grid, n_jobs=-1, cv=kfold)
# 
# 
# xg_grid.fit(x_train_re,y_train_re)
# 
# print(xg_grid.best_params_)
# 
# train_pred = xg_grid.predict(x_train_re)
# test_pred = xg_grid.predict(x_test_re)
# 
# print("Train Score: {}." .format(f1_score(y_train_re, train_pred)))
# print("Validation Score: {}." .format(f1_score(y_test_re, test_pred)))
#

## Model- 4 RF

# Commented out IPython magic to ensure Python compatibility.
# %%time
# clf_rf = RandomForestClassifier()
# 
# kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=143)
# 
# param_grid = {"n_estimators" : [3,4,5,10,12,13,14],
#               "max_depth" : [2,3,5,6],
#               "max_features" : [3,4, 5, 7],
#               "min_samples_leaf" : [4, 6, 8, 10]}
# 
# rf_grid = GridSearchCV(clf_rf, param_grid=dt_param_grid, cv=kfold)
# 
# 
# rf_grid.fit(x_train_re,y_train_re)
# 
# print(rf_grid.best_params_)
# 
# train_pred_rf = rf_grid.predict(x_train_re)
# test_pred_rf = rf_grid.predict(x_test_re)
# 
# print("Train Score: {} ." .format(f1_score(y_train_re, train_pred_rf)))
# print("Validation Score: {} ." .format(f1_score(y_test_re, test_pred_rf)))
# 
#

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

param_grid_knn = {'n_neighbors':[4,5,6]}

knn_grid = GridSearchCV(knn, param_grid=param_grid_knn, cv=5)


knn_grid.fit(x_train_re,y_train_re)

print(knn_grid.best_params_)

train_pred_rf = knn_grid.predict(x_train_re)
test_pred_rf = knn_grid.predict(x_test_re)

print("Train Score: {} ." .format(f1_score(y_train_re, train_pred_rf)))
print("Validation Score: {} ." .format(f1_score(y_test_re, test_pred_rf)))



"""# Models using Label Encoding."""

#convert floats into int

for col in ['TotalWorkingHours','Billable_Hours','Hours_off_Duty','Touring_Hours']:
  train_copy[col] = train_copy[col].astype('int')

#Do the same on the test data 
for col in ['TotalWorkingHours','Billable_Hours','Hours_off_Duty','Touring_Hours']:
  test_copy[col] = test_copy[col].astype('int')

#on training data

for col in ['Sex','Designation','NoOfProjects','joining_year','joining_month']:
  train_copy[col] = train_copy[col].astype('object')
#on testing data 

for col in ['Sex','Designation','NoOfProjects','joining_year','joining_month']:
  test_copy[col] = test_copy[col].astype('object')

train_copy['Left_Company'] = train_copy['Left_Company'].astype('category')

del train_copy['Left_Company']



"""### Encoding the data using Label encoder"""

#pass the label encoded data to the random forest Model

for x in train_copy.columns:
  if train_copy[x].dtype == 'object':
        lbl = preprocessing.LabelEncoder()
        lbl.fit(list(train_copy[x].values))
        train_copy[x] = lbl.transform(list(train_copy[x].values))

train_copy.head()

x_train_l, x_test_l, y_train_l, y_test_l = train_test_split(train_copy, y, test_size= 0.3, random_state=12, stratify= y)

test_copy.head()



"""### The training data is insufficient & it is underfitting when building the models. 


### The target labelled data is class imbalanced & should perform SMOTE method to over sample the data, It may be helpful in building the model without underfitting. 
"""



"""### Feature Engineering can be done by using the Job_History column by counting the no of companies he worked earlier & make better predictions. """



"""# Deep Learning Techniques : """

#importing packages 
import tensorflow as tf 
import keras
from keras import Sequential
from keras.layers import Dense, BatchNormalization, Dropout
from keras.layers import Activation

# chceking the splitted data 
print(x_train_re.shape)
print(x_test_re.shape)
print(y_train_re.shape)
print(y_test_re.shape)

#chcecking the label encoded  data 

print(x_train_l.shape)
print(x_test_l.shape)
print(y_train_l.shape) 
print(y_test_l.shape)

x_train_l.dtypes

model = Sequential()

#layer-1
model.add(Dense(6,kernel_initializer='glorot_uniform', input_dim=283))
# model.add(BatchNormalization())
model.add(Activation('relu'))

#layer -2 

#model.add(Dense(6, kernel_initializer='glorot_uniform', activation='relu'))
#model.add(BatchNormalization())

#layer-3 -Output layer 

model.add(Dense(1, activation='softmax', kernel_initializer='glorot_normal'))

#compiling the model 

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model_1 = model.fit(std_x, y, epochs=100, batch_size=22, validation_split=0.1)

model_1

