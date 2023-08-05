from fastapi import FastAPI
from managers.CabManagers import CabManagers
from managers.RiderManagers import RiderManagers
from managers.TripManagers import TripManagers
from routers import CabRouter#,RiderRouter
from exceptions import *
from strategies.DefaultCabMatchingStrategy import DefaultCabMatchingStrategy
from strategies.DefaultPricingStrategy  import DefaultPriceStrategy

app = FastAPI()

cabsManager = CabManagers()
ridersManager = RiderManagers()
cabMatchingStrategy = DefaultCabMatchingStrategy()
pricingStrategy = DefaultPriceStrategy()

tripsManager = TripManagers(cabsManager, ridersManager, cabMatchingStrategy, pricingStrategy)

app.include_router(CabRouter.router)
#app.include_router(RiderRouter.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
    