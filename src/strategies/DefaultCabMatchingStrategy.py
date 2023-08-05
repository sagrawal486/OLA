from .CabMatchingStrategy import CabMatchingStrategy

class DefaultCabMatchingStrategy(CabMatchingStrategy):

    def matchCabToRider(self, rider, candidateCabs, fromPoint, toPoint):
        # Implementation for matchCabToRider
        if len(candidateCabs) == 0:
            return None
        else:
            return candidateCabs[0]
    