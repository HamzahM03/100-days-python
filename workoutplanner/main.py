import os
from dotenv import load_dotenv
import requests
from datetime import datetime

SHEETY_POST_REQ = "https://api.sheety.co/0479a416138c10960be573fca1167350/workoutTracking/workouts"

#Get current date and time for workout log entry
date = datetime.now()
today_date = date.strftime("%d/%m/%Y")
today_time = date.strftime("%H:%M:%S")


load_dotenv()  # loads from .env into environment

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")
NUTRI_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

if not API_KEY or not APP_ID:
    raise ValueError("Missing APP_ID or API_KEY. Check your .env file!")

#Headers required by Nutritionix API for authentication
nutri_auth_params = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

#User's exercise input passed as the JSON body
nutri_query = {
    "query": input("What exercises did you do today?")
}

nutri_response = requests.post(url=NUTRI_EXERCISE_ENDPOINT,json=nutri_query, headers=nutri_auth_params)
if nutri_response.status_code != 200:
    print("Error:", nutri_response.status_code, nutri_response.text)
    exit()

#Grab the data from the server's response
nutri_data = nutri_response.json()
first_exercise = nutri_data["exercises"][0]
exercise = first_exercise["user_input"].title()
duration_of_exercise = first_exercise["duration_min"]
calories_burned = first_exercise["nf_calories"]

#Print exercise summary for verification
print(f"Exercise: {exercise}\nDuration of exercise: {duration_of_exercise}\nCalories burned {calories_burned}")

#Check sheety_query API https://sheety.co/docs/requests.html, this allows us to add rows to our Google spreadsheet through script
sheety_query = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise,
        "duration": duration_of_exercise,
        "calories": calories_burned
    }
}

#Authorization token for secure Sheety API access
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

#Adding the token to the header to be passed in my post request to Sheety add row endpoint
sheety_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

sheety_response = requests.post(url=SHEETY_POST_REQ, json=sheety_query, headers=sheety_headers)
sheety_data = sheety_response.json()

#Print Sheety API response for confirmation
print(sheety_response.text)
print(sheety_data)


