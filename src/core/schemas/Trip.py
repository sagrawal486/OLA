from pydantic import BaseModel
from .Rider import Rider
from .Location import Location
from math import pow, sqrt
from enum import Enum
from typing import Optional
import  typing

# if typing.TYPE_CHECKING:
#     from .Cab import Cab  # Importing Cab only for type checking

class TripStatus(Enum):
  IN_PROGRESS = 1
  FINISHED = 2

class Trip(BaseModel):
    rider: Rider
    cab: str
    status: TripStatus
    price: float
    fromPoint: Location
    toPoint: Location

    def __init__(self,rider: Rider, cab:  int, price: float, fromPoint: Location, toPoint: Location):
      super().__init__(rider = rider, cab = cab, price = price, fromPoint = fromPoint, toPoint = toPoint,status = TripStatus.IN_PROGRESS)
        # self.rider = rider
        # self.cab    = cab
        # self.price = price
        # self.fromPoint  = fromPoint
        # self.toPoint = toPoint
        # self.status = TripStatus.IN_PROGRESS

    def endTrip(self):
        self.status = TripStatus.FINISHED

