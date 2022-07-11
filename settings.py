import os

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

OPENWEATHER_TOKEN = token  
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_TOKEN + "&lang=ru&"
    "units=metric"
)
REFRESH_TIME_MIN = 10
