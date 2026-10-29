
import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env")

url = f"https://api.openweathermap.org/data/2.5/forecast?q=Jakarta&units=metric&appid={API_KEY}"


def fetch_response(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    return data 


def main():
    data = fetch_response(url)
    data_list = data["list"]
    seen_dates = set()
    weather_list = []
    for item in data_list:
        date_item= item["dt_txt"].split(" ")
        date = date_item[0]
        
        if date not in seen_dates:
            seen_dates.add(date)
            temp = str(item["main"]["temp"])
            formatted = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%a, %b %d %Y:")
            dates_weather = f"{formatted} {temp}° C"
            weather_list.append(dates_weather)
            
    print("Weather Forecast:")
    for item in weather_list:
        print(item)
        

if __name__ == "__main__":
    main()
