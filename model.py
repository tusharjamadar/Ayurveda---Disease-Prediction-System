# Importing libraries
import numpy as np
import pandas as pd
import warnings
from scipy.stats import mode
import pickle

warnings.filterwarnings('ignore')

# svm_model
svm_model=pickle.load(open('svm_model.pkl','rb'))

#nb_model
nb_model=pickle.load(open('nb_model.pkl','rb'))

#rf_model
rf_model=pickle.load(open('rf_model.pkl','rb'))

#dt_model
dt_model=pickle.load(open('dt_model.pkl','rb'))

#symptoms
symptoms=pickle.load(open('symptoms.pkl','rb'))

#encoder
encoder=pickle.load(open('encoder.pkl','rb'))

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index
 
data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":encoder.classes_
}

def predictDisease(symptoms):
    symptoms = symptoms.split(",")
     
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        if(symptom != "null"):
            index = data_dict["symptom_index"][symptom]
            input_data[index] = 1
         
    input_data = np.array(input_data).reshape(1,-1)
     
    rf_prediction = data_dict["predictions_classes"][rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][svm_model.predict(input_data)[0]]
    dt_prediction = data_dict["predictions_classes"][dt_model.predict(input_data)[0]]
     
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction,dt_prediction])[0][0]
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": nb_prediction,
        "decisionTree_model_prediction": dt_prediction,
        "final_prediction":final_prediction
    }
    return predictions

 
# result = predictDisease("Itching,Skin Rash,Nodal Skin Eruptions,Acidity")
# print(result["final_prediction"])