from exceptions.TripNotFoundException import TripNotFoundException
from exceptions.NoCabsAvailableException import NoCabsAvailableException
from core.schemas.Trip import Trip

class TripManagers:

    MAX_ALLOWED_TRIP_MATCHING_DISTANCE = 10.0;
    trips = {}

    def __init__(self,cabsManager, ridersManager,cabMatchingStrategy, pricingStrategy) -> None:
        self.ridersManager = ridersManager
        self.cabsManager = cabsManager
        self.cabMatchingStrategy = cabMatchingStrategy
        self.pricingStrategy = pricingStrategy

    def createTrip(self,rider, fromPoint, toPoint):
        closeByCabs = self.cabsManager.getCabs(fromPoint, self.MAX_ALLOWED_TRIP_MATCHING_DISTANCE)    
        closeByAvailableCabs = []
        for cab in closeByCabs:
            if closeByCabs[cab].currentTrip is None:
                closeByAvailableCabs.append(closeByCabs[cab])

        selectedCab = self.cabMatchingStrategy.matchCabToRider(rider, closeByAvailableCabs, fromPoint, toPoint)
        if selectedCab is None:
            raise NoCabsAvailableException("No Can Available Exception")

        price = self.pricingStrategy.findPrice(fromPoint, toPoint)
        newTrip = Trip(rider, selectedCab.id, price, fromPoint, toPoint)
        if (self.trips.get(rider.id) is None):
            self.trips[rider.id] = []
        self.trips[rider.id].append(newTrip)
        selectedCab.currentTrip = newTrip

    def tripHistory(self,rider):

        return self.trips.get(rider.id)

    def endTrip(self, cab):
        if (cab.currentTrip is None):
            raise TripNotFoundException("Trip not found")

        cab.currentTrip.endTrip()
        cab.currentTrip = None


