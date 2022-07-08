from typing import NamedTuple
import subprocess as sp
import re
import time

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_location() -> Coordinates:
    return Coordinates(latitude=10, longitude=20)
