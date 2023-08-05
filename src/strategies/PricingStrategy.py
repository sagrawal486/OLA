from abc import ABC, abstractmethod
from core.schemas.Location import Location

class PricingStrategy(ABC):
    @abstractmethod
    def findPrice(self,fromPoint: Location, toPoint: Location):
        pass