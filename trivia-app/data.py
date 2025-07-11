import requests
API_URL = "https://opentdb.com/api.php?amount=10"
parameters = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get(url=API_URL, params=parameters).json()["results"]


question_data = data
