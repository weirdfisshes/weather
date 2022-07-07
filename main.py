from location import get_location
from weather import get_weather
from printer import print_weather


def main():
    location = get_location()
    weather = get_weather(location)
    print(print_weather(weather))


if __name__ == '__main__':
    main()