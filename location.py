from typing import NamedTuple
import geocoder


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_location() -> Coordinates:
    location = geocoder.ip('me')
    latitude = location.latlng[0]
    longitude = location.latlng[1]
    return Coordinates(latitude=latitude, longitude=longitude)


