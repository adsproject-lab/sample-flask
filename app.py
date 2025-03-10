from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    application_id = os.getenv("APPLICATION_ID")
    return render_template('index.html', application_id=application_id)

@app.route('/get_jwt')
def get_jwt():
    url = "https://api.goentri.com/token"
    application_id = os.getenv("APPLICATION_ID")
    secret = os.getenv("API_SECRET")

    response = requests.post(url, json={
        "applicationId": application_id,
        "secret": secret
    })
    
    if response.status_code == 200:
        token = response.json().get("auth_token")
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Failed to retrieve token"}), 500
