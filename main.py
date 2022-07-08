from location import get_location
from exceptions import ApiServiceError, CantGetCoordinates
from weather_api import get_weather
from printer import format_weather


def main():
    try:
        coordinates = get_location()
    except CantGetCoordinates:
        print("Не удалось получить GPS координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Не удалось получить погоду по координатам {coordinates}")
        exit(1)
    print(format_weather(weather))


if __name__ == "__main__":
    main()