from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = os.getenv("API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if str(data.get("cod")) != "200":
        return render_template("weather.html", error="City not found....")
    
    weather_info = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": round(data["main"]["temp"], 1),
        "desc": data["weather"][0]["description"].capitalize(),
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"]
    }

    return render_template("weather.html", weather=weather_info)

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))