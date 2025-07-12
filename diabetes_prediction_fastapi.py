from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.responses import JSONResponse
from typing import Literal

app = FastAPI()

class ModelInput(BaseModel):
    gender: Literal['Female', 'Male', 'Other']
    age: int
    hypertension: int
    heart_disease: int
    smoking_history_cleaned: Literal['never', 'unknown', 'current', 'past']
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int

diabetes_model = joblib.load("diabetes_prediction_rfc.pkl")

@app.post('/diabetes_prediction')
def predict_diabetes(input_parameters : ModelInput):
    try:
        input_df = pd.DataFrame([input_parameters.model_dump()])

        prediction = diabetes_model.predict(input_df)

        result = {
            "prediction": int(prediction[0]),
            "message": "This patient HAS Diabetes" if prediction[0] == 1 else "This patient DOES NOT have Diabetes"
        }
        return JSONResponse(content=result)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get("/")
def root():
    return {"message": "Diabetes prediction API is running"}