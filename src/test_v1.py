

from routers.CabRouter import CabRouter
from routers.RiderRouter import RidersRouter
from managers.CabManagers import CabManagers
from managers.TripManagers import TripManagers
from managers.RiderManagers import RiderManagers
from strategies.DefaultCabMatchingStrategy import DefaultCabMatchingStrategy
from strategies.DefaultPricingStrategy import DefaultPriceStrategy
from exceptions.RiderAlreadyExistsException import RiderAlreadyExistsException
from exceptions.CabAlreadyExistsException import CabAlreadyExistsException
from exceptions.CabNotFoundException import CabNotFoundException
from exceptions.NoCabsAvailableException import NoCabsAvailableException
from exceptions.RiderNotFoundException import RiderNotFoundException

def test_cab_booking_flow():
    cabs_manager = CabManagers()
    riders_manager = RiderManagers()

    cab_matching_strategy = DefaultCabMatchingStrategy()
    pricing_strategy = DefaultPriceStrategy()

    trips_manager = TripManagers(cabs_manager, riders_manager, cab_matching_strategy, pricing_strategy)

    cabs_controller = CabRouter(cabs_manager, trips_manager)
    riders_controller = RidersRouter(riders_manager, trips_manager)

    r1 = "r1"
    riders_controller.register_rider({"riderId": r1, "riderName": "ud"})
    r2 = "r2"
    riders_controller.register_rider({"riderId": r2, "riderName": "du"})
    r3 = "r3"
    riders_controller.register_rider({"riderId": r3, "riderName": "rider3"})
    r4 = "r4"
    riders_controller.register_rider({"riderId": r4, "riderName": "rider4"})

    c1 = "c1"
    cabs_controller.register_cab({"cabId": c1, "driverName": "driver1"})
    c2 = "c2"
    cabs_controller.register_cab({"cabId": c2, "driverName": "driver2"})
    c3 = "c3"
    cabs_controller.register_cab({"cabId": c3, "driverName": "driver3"})
    c4 = "c4"
    cabs_controller.register_cab({"cabId": c4, "driverName": "driver4"})
    c5 = "c5"
    cabs_controller.register_cab({"cabId": c5, "driverName": "driver5"})

    cabs_controller.update_cab_location(c1, 1.0, 1.0)
    cabs_controller.update_cab_location(c2, 2.0, 2.0)  # na
    cabs_controller.update_cab_location(c3, 100.0, 100.0)
    cabs_controller.update_cab_location(c4, 110.0, 110.0)  # na
    cabs_controller.update_cab_location(c5, 4.0, 4.0)

    cabs_controller.update_cab_availability(c2, False)
    cabs_controller.update_cab_availability(c4, False)

    riders_controller.book(r1, 0.0, 0.0, 500.0, 500.0)
    riders_controller.book(r2, 0.0, 0.0, 500.0, 500.0)

    print("\n### Printing current trips for r1 and r2")
    print(riders_controller.fetch_history(r1))
    print(riders_controller.fetch_history(r2))

    cabs_controller.update_cab_location(c5, 50.0, 50.0)

    print("\n### Printing current trips for r1 and r2")
    print(riders_controller.fetch_history(r1))
    print(riders_controller.fetch_history(r2))

    cabs_controller.end_trip(c5)

    print("\n### Printing current trips for r1 and r2")
    print(riders_controller.fetch_history(r1))
    print(riders_controller.fetch_history(r2))

    try:
        riders_controller.book(r3, 0.0, 0.0, 500.0, 500.0)
    except Exception as E:
        print("No cabs available for booking.")

    riders_controller.book(r4, 48.0, 48.0, 500.0, 500.0)
    print("\n### Printing current trips for r1, r2 and r4")
    print(riders_controller.fetch_history(r1))
    print(riders_controller.fetch_history(r2))
    print(riders_controller.fetch_history(r4))

    try:
        riders_controller.book("abcd", 0.0, 0.0, 500.0, 500.0)
    except Exception as E:
        print("Rider not found.")

    try:
        riders_controller.register_rider("r1", "shjgf")
    except Exception as E:
        print("Rider already exists.")

    try:
        cabs_controller.register_cab("c1", "skjhsfkj")
    except Exception as E:
        print("Cab already exists.")

    try:
        cabs_controller.update_cab_location("shss", 110.0, 110.0)
    except Exception as E:
        print("Cab not found.")

    try:
        cabs_controller.update_cab_availability("shss", False)
    except Exception as E:
        print("Cab not found.")

# Run the test
test_cab_booking_flow()
