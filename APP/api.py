from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

from fastapi.middleware.cors import CORSMiddleware


app= FastAPI(title="Loan Default Prediction API")
model = joblib.load("loan_default_pipeline.pkl")

f_columns = joblib.load("feature_columns.pkl") 


class LoanInput(BaseModel):
    loan_amnt: float
    term: int
    int_rate: float
    installment: float
    emp_length: float
    annual_inc: float
    verification_status: int
    dti: float
    delinq_2yrs: float
    inq_last_6mths: float
    open_acc: float
    pub_rec: float
    revol_bal: float
    revol_util: float
    total_acc: float
    grade: str
    home_ownership: str


@app.post("/predict")


def predictRisk(data:LoanInput):
    df = pd.DataFrame([data.dict()])
    df = pd.get_dummies(df, columns=["grade", "home_ownership"])
    df = df.reindex(columns=f_columns, fill_value=0)

    get_risk = model.predict_proba(df)[0][1]

    return {
    "default_probability": float(get_risk),
    "risk": "High Risk" if get_risk > 0.5 else "Low Risk"
   }



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)