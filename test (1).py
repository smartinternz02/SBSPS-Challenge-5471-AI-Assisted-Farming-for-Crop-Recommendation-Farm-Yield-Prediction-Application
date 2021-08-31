from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')

import requests
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":'SOoRwv8GBuqaE6NCR4YWL1SwplbSQsP-HUAp83k-WlHQ' , "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["humidity","K","N","P","ph","rainfall","temperature"], "values": [[80,56,78,78,78,78,78]]}]}

response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/9c65d690-7912-42ca-84a3-396eb7dbd624/predictions?version=2021-08-26', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
