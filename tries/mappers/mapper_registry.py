

class MapperRegistry:

    def __init__(self):
        self.mappers = {}


    def getMapperFor(self, classObject):
        return self.mappers.get(classObject, None)


    def setMapperFor(self, classObject, mapper):
        self.mappers.update({classObject: mapper})


mapperRegistry = MapperRegistry()