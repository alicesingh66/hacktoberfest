import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
APP_IP = "a12dbdc0"
APP_KEY = "94d5f1f979bad17d11b4f521c45d2d7b"
GENDER = "female"
WEIGHT_KG = "60"
HEIGHT_CM = "162"
AGE = "20"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
QUERY = input('Enter your physical activity and the covered distances.')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/b1d2703a04c50ba31c8d18a71b25508f/copyOfMyWorkouts/workouts"

basic = HTTPBasicAuth('AliceSingh6666', 'qwertyuiopasdfghjkl')


header = {
    "x-app-id": APP_IP,
    "x-app-key": APP_KEY,
    #"Content-Type": "application/json",
}

parameters = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=header)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=basic)

    print(sheet_response.text)
