from pydantic import BaseModel, Field
from .Trip import Trip
from .Location import Location
from typing import Optional

class Cab(BaseModel):
    id: str
    driverName: str
    currentTrip: Optional[Trip] = Field(default=None)
    currentLocation: Optional[Location] = Field(default=None)
    isAvailable: bool = Field(default=True)

    def __init__(self, id: int, driverName: str):
        super().__init__(id=id, driverName=driverName)

    def __str__(self):
        return f"Cab[" + \
        "id='" + self.id + '\'' + \
        ", driverName='" + self.driverName + '\'' + \
        ", currentLocation=" + self.currentLocation + \
        ", isAvailable=" + self.isAvailable + \
        '}'

    # @property
    # def  id(self):
    #     return self.id

    # @property
    # def  driverName(self):
    #     return self.driverName

    # @property
    # def  currentLocation(self):
    #     return self.currentLocation

    # @currentLocation.setter
    # def  currentLocation(self,value):
    #     self.currentLocation = value

    # @property
    # def  currentTrip(self):
    #     return self.currentTrip

    # @currentTrip.setter
    # def  currentTrip(self,value):
    #     self.currentTrip = value

    # @property
    # def  isAvailable(self):
    #     return self.isAvailable

    # @isAvailable.setter
    # def  isAvailable(self,value):
    #     self.isAvailable = value

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