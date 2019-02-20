

class VehicleMapper:

    def __init__(self, identityMap, databaseWrapper):

        self.identityMap = identityMap
        self.databaseWrapper = databaseWrapper


    def find(self, primaryKey):

        obj =  self.identityMap.get(primaryKey)

        if obj is not None:
            return obj

        else:
            self.databaseWrapper.select('Vehicle', primaryKey)