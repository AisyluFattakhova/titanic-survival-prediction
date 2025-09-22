# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd


# Relative path to models folder in the container
filename = "models/logistic_regression_model.pkl"

with open(filename, "rb") as f:
    model = pickle.load(f)


# Initialize FastAPI app
app = FastAPI()

# Define the request body schema (must match training features)
class Passenger(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str

@app.get("/")
def root():
    return {"message": "Titanic Survival Prediction API is running!"}

@app.post("/predict")
def predict(passenger: Passenger):
    # Convert request to DataFrame
    data = pd.DataFrame([passenger.dict()])

    # Make prediction
    prediction = model.predict(data)[0]

    return {"prediction": int(prediction)}
