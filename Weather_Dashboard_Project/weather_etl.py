import os
import requests
import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

# Loads API Key from .env
load_dotenv()
API_KEY = os.getenv("VC_API_KEY")

cities = ["Chicago, IL","Minneapolis, MN","Des Moines, IA","Indianapolis, IN","ST Louis, MO"]
# date = "2023-03-01"
end_date = datetime.today()
start_date = end_date - relativedelta(years=5)

dates = []
current_date = start_date.replace(day=1)

while current_date <= end_date:
    dates.append(current_date.strftime("%Y-%m-%d"))
    current_date += relativedelta(months=1)


conn = sqlite3.connect('weather.db')
cur = conn.cursor()
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

for city in cities:
    print(f"\n\nStarting data for {city}...")
    for date in dates:
        
        url = f"{base_url}/{city}/{date}?uniGroup=us&key={API_KEY}&include=days"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                day = data['days'][0]

                temp = day.get('temp')
                temp_min = day.get('tempmin')
                temp_max = day.get('tempmax')
                precip = day.get('precip')
                cond = day.get('conditions')


                cur.execute('''
                    INSERT INTO weather (city, date, temp, temp_min, temp_max, precip, cond)
                    VALUES (?,?,?,?,?,?,?)
                    ''', (city, date, temp, temp_min, temp_max, precip, cond))
                conn.commit()
                print(f" {date} | {city} saved")
            else:
                print(f" {date} | {city} failed. Status: {response.status_code}")
        except Exception as e:
            print(f" Error for {city} on {date}: {e}")

conn.close()
print('\n\n ALL DATA SAVED TO weather.db')