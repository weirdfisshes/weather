from weather_api import Weather

def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (
        f"{weather.city}, температура {weather.temperature}°C, "
        f"{weather.weather_type}\n"
    )


if __name__ == "__main__":
    print('Для работы с программой запустите файл main.py')