from abc import ABC, abstractmethod
from core.schemas.Rider import Rider
from core.schemas.Cab import Cab
from core.schemas.Location import Location

class CabMatchingStrategy(ABC):
    @abstractmethod
    def matchCabToRider(self,rider,candidateCabs , fromPoint,toPoint):
        pass