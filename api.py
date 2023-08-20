from fastapi import FastAPI
import os, uvicorn
from typing import List, Literal
from pydantic import BaseModel
import joblib
from fastapi.encoders import jsonable_encoder


#CONFIG
app = FastAPI(
title = "Sepsis Classification Web App",
version = "0.0.1",
description = "This App allows users to predict whether a patient would be diagnosed with Septsis or not"

)

# #API INPUT
class Input(BaseModel):
    Plasma_Glucose: int
    Blood_Work_Result1: int
    Blood_Pressure: int
    Blood_Work_Result2: int
    Blood_Work_Result3: int
    Body_Mass_Index: float
    Blood_Work_Result4: float
    Age: int
    Insurance: int
    


#ENDPOINT
@app.get("/")
async def root():
    return{"message": "Online"}

@app.post("/predict")
def predict(input: Input):
    scaler = joblib.load("Assets/scaler.joblib")
    model = joblib.load("Assets/model.joblib")
    
    features = [input.Plasma_Glucose, 
input.Blood_Work_Result1, 
input.Blood_Pressure,
input.Blood_Work_Result2,
input.Blood_Work_Result3,
input.Body_Mass_Index,
input.Blood_Work_Result4,
input.Age,input.Insurance]


    scaled_features = scaler.transform([features])[0]
    prediction = model.predict([scaled_features])[0]
    
    # Serialize the prediction result using jsonable_encoder
    serialized_prediction = jsonable_encoder({"prediction": int(prediction)})
    if serialized_prediction["prediction"] == 1:
        Diagnosis = {"Results" : "Positive"}
    else:
        Diagnosis = {"Results" : "Negative"}
    return Diagnosis


if __name__ == '__main__':
    uvicorn.run('api:app', reload =True)
