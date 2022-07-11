from typing import NamedTuple

import geocoder

from exceptions import GetLocationFailed

class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_location() -> Coordinates:
    try:
        location = geocoder.ip('me')
        latitude = location.latlng[0]
        longitude = location.latlng[1]
        return Coordinates(latitude=latitude, longitude=longitude)
    except:
        raise GetLocationFailed


if __name__ == "__main__":
    print('Для работы с программой запустите файл main.py')
