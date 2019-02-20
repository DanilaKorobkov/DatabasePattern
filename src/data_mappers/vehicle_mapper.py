from .i_mapper import *


class VehicleMapper(IMapper):

    def find(self, primaryKey):

        obj =  self.identityMap.get(primaryKey)

        if obj is not None:
            return obj

        else:
            self.databaseWrapper.select('Vehicle', primaryKey)


    def add(self, obj):
        raise NotImplementedError

    def update(self, obj):
        raise NotImplementedError

    def remove(self, primaryKey):
        raise NotImplementedError