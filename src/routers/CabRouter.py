from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from managers.CabManagers import CabManagers
from managers.TripManagers import TripManagers
from core.schemas.Cab import Cab
from core.schemas.Location import Location
#from main import cabsManager,tripsManager,ridersManager

app = FastAPI()

class CabRouter:


    def __init__(self, cabsManager, tripsManager) -> None:
        self.cabsManager = cabsManager
        self.tripsManager = tripsManager

    def register_cab(self, cab: Cab):
        cab_id = cab.get('cabId')
        driver_name = cab.get('driverName')
        self.cabsManager.createCab(Cab(cab_id, driver_name))
        return JSONResponse(content=f"{cab_id} {driver_name} Cab Created Successfully", status_code=200)

    def update_cab_location(self,cabId: str, x: float, y: float):
        self.cabsManager.updateCabLocation(cabId, Location(x, y))
        return JSONResponse(content=f"{cabId} {x,y} Location Updated Successfully", status_code=200)
    
    def update_cab_availability(self, cabId: str, newAvailability: bool):
        self.cabsManager.updateCabAvailability(cabId, newAvailability)
        return JSONResponse(content="{cab_id} {newAvailability} Updated Cab Availability Successfully", status_code=200)

    def end_trip(self, cabId: str):
        self.tripsManager.endTrip(self.cabsManager.getCab(cabId))
        return JSONResponse(content="{cab_id} End Trip Successfully", status_code=200)
