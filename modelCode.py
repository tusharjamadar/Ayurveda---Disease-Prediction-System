# Importing libraries
import numpy as np
import pandas as pd
import warnings
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

warnings.filterwarnings('ignore')

# Reading the train.csv by removing the
# last column since it's an empty column
data = pd.read_csv("Training.csv").dropna(axis = 1)

# Encoding the target value into numerical
# value using LabelEncoder
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

X = data.iloc[:,:-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size = 0.2, random_state = 24)

# Training the models on whole data
final_svm_model = SVC()
final_nb_model = GaussianNB()
final_rf_model = RandomForestClassifier(random_state=18)
final_dt_model = DecisionTreeClassifier(splitter='best', criterion='entropy', min_samples_leaf=2)

final_svm_model.fit(X, y)
final_nb_model.fit(X, y)
final_rf_model.fit(X, y)
final_dt_model.fit(X, y)


# svm_model
pickle.dump(final_svm_model,open('svm_model.pkl','wb'))

#nb_model
pickle.dump(final_nb_model,open('nb_model.pkl','wb'))

#rf_model
pickle.dump(final_rf_model,open('rf_model.pkl','wb'))

#dt_model
pickle.dump(final_dt_model,open('dt_model.pkl','wb'))

symptoms = X.columns.values

# #symptoms
pickle.dump(symptoms,open('symptoms.pkl','wb'))

#rf_model
pickle.dump(encoder,open('encoder.pkl','wb'))