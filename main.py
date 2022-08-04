from email.errors import HeaderParseError
import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
SHEET_TOKEN = ""

sheety_endpoint = ""
nutritionix_endpoint = ""

nutrinionix_headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id" : "0"
}

nutritionix_parameters = {
    "query" : input("What exercises have you done today? "),
    "gender" : "male",
    "age" : 21
}

response = requests.post(url=nutritionix_endpoint, headers=nutrinionix_headers, json=nutritionix_parameters)
response.raise_for_status()
data = response.json()

todays_date = datetime.now().strftime(r"%d/%m/%Y")
todays_time = datetime.now().strftime(r"%X")

for exercise in data["exercises"]:
    sheet_input = {
        "workout": 
            {
                "date": todays_date,
                "time": todays_time,
                "exercise": exercise["name"].title(),
                "duration" : exercise["duration_min"],
                "calories" : exercise["nf_calories"]
            }
    }
    sheet_headers = {
        "Authorization" : SHEET_TOKEN
    }
    response = requests.post(url=sheety_endpoint, json=sheet_input, headers=sheet_headers)
    response.raise_for_status()
    print(response)
