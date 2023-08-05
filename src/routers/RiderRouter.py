from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from managers.CabManagers import CabManagers
from managers.TripManagers import TripManagers
from core.schemas.Rider import Rider
from core.schemas.Location import Location

class RidersRouter:
    def __init__(self, ridersManager, tripsManager):
        self.ridersManager = ridersManager
        self.tripsManager = tripsManager

    def register_rider(self, rider: Rider):
        riderId = rider.get('riderId')
        riderName = rider.get('riderName')
        self.ridersManager.createRider(Rider(riderId, riderName))
        return JSONResponse(content=f"{riderId} {riderName} Rider Created Successfully",status_code=200)

    def book(self, riderId: str, sourceX: float, sourceY: float, destX:float, destY: float):
        self.tripsManager.createTrip(
            self.ridersManager.getRider(riderId),
            Location(sourceX, sourceY),
            Location(destX, destY))
        return JSONResponse(content="{rider.riderId} Created Trip Successfully",status_code=200)

    def fetch_history(self, riderId: str):
        trips = self.tripsManager.tripHistory(self.ridersManager.getRider(riderId))
        return trips