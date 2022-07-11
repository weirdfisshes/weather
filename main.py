from location import get_location
from exceptions import GetLocationFailed, GetWeatherFailed
from weather_api import get_weather
from printer import format_weather


def main():
    try:
        coordinates = get_location()
    except GetLocationFailed:
        print("Не удалось получить GPS координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except GetWeatherFailed:
        print(f"Не удалось получить погоду по координатам {coordinates}")
        exit(1)
    print(format_weather(weather))


if __name__ == "__main__":
    main()