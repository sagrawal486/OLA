from pydantic import BaseModel, Extra
from math import pow, sqrt

class Location(BaseModel):
    x: float
    y: float

    def __init__(self, x, y) -> None:
        super().__init__(x = x, y = y)

    def distance (self, location2 ):
        return sqrt( pow(self.x - location2.x, 2) + pow(self.y - location2.y, 2) )
    