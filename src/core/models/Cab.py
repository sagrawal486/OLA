from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel, Extra
from . import Trip, Location

class Cab(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    driverName: str
    currentTrip: Trip
    currentLocation: Location
    isAvailable: bool
    
# cab_1 = Cab(id = 1,driverName="Deadpond")
# cab_2 = Cab(id = 2,driverName="Spider-Boy")
# cab_3 = Cab(id = 3, driverName="Rusty-Man")

# engine = create_engine("sqlite:///database.db")

# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(cab_1)
#     session.add(cab_2)
#     session.add(cab_3)
#     session.commit()

# with Session(engine) as session:
#     statement = select(Cab).where(Cab.driverName == "Spider-Boy")
#     hero = session.exec(statement).first()
#     print(hero)