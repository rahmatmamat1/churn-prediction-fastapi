import json
import pickle
import uvicorn

from fastapi import FastAPI, Request

from pydantic import BaseModel

class Costumer(BaseModel):
    gender: str
    seniorcitizen: int
    partner: str
    dependents: str
    phoneservice: str
    multiplelines: str
    internetservice: str
    onlinesecurity: str
    onlinebackup: str
    deviceprotection: str
    techsupport: str
    streamingtv: str
    streamingmovies: str
    contract: str
    paperlessbilling: str
    paymentmethod: str
    tenure: int
    monthlycharges: float
    totalcharges: float

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI()

@app.post('/predict/')
# async def predict(customer: Request):
async def predict(customer: Costumer):

    # customer = await customer.json()
    customer_dict = customer.dict()

    X = dv.transform([customer_dict])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return result


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9696)