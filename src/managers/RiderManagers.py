from exceptions import RiderNotFoundException, RiderAlreadyExistsException

from core.schemas.Rider import Rider

class RiderManagers:

    riders = {}

    def createRider(self, newRider):
        if (self.riders.get(newRider.id)):
            raise RiderAlreadyExistsException("Rider alaready exists")
        self.riders[newRider.id] =  newRider

    def getRider(self,riderId):
        if self.riders.get(riderId) is None:
            raise RiderNotFoundException("Rider Not found");
        return self.riders.get(riderId);
