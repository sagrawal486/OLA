from .PricingStrategy import PricingStrategy

class DefaultPriceStrategy(PricingStrategy):

    PER_KM_RATE = 10.0;

    def findPrice(self, fromPoint, toPoint):
        # Implementation for matchCabToRider
        return fromPoint.distance(toPoint) * self.PER_KM_RATE;
    