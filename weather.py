from enum import Enum
from typing import NamedTuple

from location import Coordinates

Celsius = int


class TypeOfWeather(Enum):
    CLEAR = 'Ясно'

class Weather(NamedTuple):
    temp: Celsius
    type: TypeOfWeather

def get_weather(coordinates: Coordinates) -> Weather:
    return Weather(
        temp = 20,
        type = TypeOfWeather.CLEAR
    )