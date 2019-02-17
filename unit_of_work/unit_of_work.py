# Internal
# Python

class UnitOfWork:

    def __init__(self):

        self.newObjects = []
        self.dirtyObjects = []
        self.removedObjects = []


    def registerNew(self, obj):

        assert obj.id is not None

        assert obj not in self.dirtyObjects
        assert obj not in self.removedObjects
        assert obj not in self.newObjects

        self.newObjects.append(obj)


    def registerDirty(self, obj):

        assert obj.id is not None

        assert obj not in self.removedObjects
        assert obj not in self.newObjects
        assert obj not in self.dirtyObjects

        self.newObjects.append(obj)


    def registerRemoved(self, obj):

        assert obj.id is not None

        if obj in self.newObjects:
            self.newObjects.remove(obj)

        self.dirtyObjects.remove(obj)

        if obj not in self.removedObjects:
            self.removedObjects.append(obj)


    # Объект считанный из базы данных
    def registerClean(self, obj):
        pass


    def commit(self):

        self.insertNew()
        self.updateDirty()
        self.deleteRemoved()


    def insertNew(self):

        for obj in self.newObjects:
            # objectMapper = MapperRegistry.getMapper(obj.__class__.__name__)
            # objectMapper.insert(obj)
            pass


    def updateDirty(self):

        for obj in self.newObjects:
            # objectMapper = MapperRegistry.getMapper(obj.__class__.__name__)
            # objectMapper.update(obj)
            pass


    def deleteRemoved(self):

        for obj in self.newObjects:
            # objectMapper = MapperRegistry.getMapper(obj.__class__.__name__)
            # objectMapper.remove(obj)
            pass