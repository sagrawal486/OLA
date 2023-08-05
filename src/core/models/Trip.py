from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel, Extra
from . import Rider, Cab, Location
from enum import Enum
 
class TripStatus(Enum):
  IN_PROGRESS = 1
  FINISHED = 2

class Trip(SQLModel, table=True):
    rider: Rider
    cab: Cab
    status: TripStatus
    price: float
    fromPoint: Location
    toPoint: Location


    