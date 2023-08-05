from exceptions import CabAlreadyExistsException, CabNotFoundException

class CabManagers:

    cabs = {}

    def __init__(self) -> None:
        pass

    def createCab(self, newCab):
        if self.cabs.get(newCab.id):
            raise CabAlreadyExistsException("Cab already exists")
        self.cabs[newCab.id] = newCab

    def getCab(self,cabId):
        if self.cabs.get(cabId) is None:
            raise CabNotFoundException("Cab not found")
        return self.cabs[cabId]
    
    def updateCabLocation(self,cabId,newLocation):
        if self.cabs.get(cabId) is None:
            raise CabNotFoundException("Cab not found")
        self.cabs.get(cabId).currentLocation = newLocation

    def updateCabAvailability(self,cabId,newAvailability):
        if self.cabs.get(cabId) is None:
            raise CabNotFoundException("Cab not found")
        self.cabs.get(cabId).isAvailable = newAvailability

    def getCabs(self, fromPoint, distance):
        result = {}
        for cab in self.cabs:
            if self.cabs[cab].isAvailable & (self.cabs[cab].currentLocation.distance(fromPoint) <= distance):
                result.update({cab:self.cabs[cab]})
        return result

