import requests
import time

url = 'http://localhost:9696/predict'
# url = 'https://churn-service-fastapi-7bb3esgl5a-uc.a.run.app/predict'

customer_id = 'xyz-123'
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": (1 * 29.85)
}

start_time = time.time()
response = requests.post(url, headers={'Content-Type': 'application/json'}, json=customer).json()
print("--- %s seconds ---" % (time.time() - start_time))

print(response)

if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)