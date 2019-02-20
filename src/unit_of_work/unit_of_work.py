# Internal
# Python

class PresentedInDatabaseObject:

    def __init__(self):
        self.id = None


    def markNew(self):
        UnitOfWork.registerNew(self)


    def markClean(self):
        UnitOfWork.registerClean(self)


    def markDirty(self):
        UnitOfWork.registerDirty(self)


    def markRemoved(self):
        UnitOfWork.registerRemoved(self)


class UnitOfWork:

    newObjects = []
    dirtyObjects = []
    removedObjects = []

    @classmethod
    def registerNew(cls, obj: PresentedInDatabaseObject):

        assert obj.id is not None

        assert obj not in cls.dirtyObjects
        assert obj not in cls.removedObjects
        assert obj not in cls.newObjects

        cls.newObjects.append(obj)


    @classmethod
    def registerDirty(cls, obj: PresentedInDatabaseObject):

        assert obj.id is not None

        assert obj not in cls.removedObjects
        assert obj not in cls.newObjects
        assert obj not in cls.dirtyObjects

        cls.newObjects.append(obj)


    @classmethod
    def registerRemoved(cls, obj: PresentedInDatabaseObject):

        assert obj.id is not None

        if obj in cls.newObjects:
            cls.newObjects.remove(obj)

        cls.dirtyObjects.remove(obj)

        if obj not in cls.removedObjects:
            cls.removedObjects.append(obj)


    @classmethod
    def registerClean(cls, obj: PresentedInDatabaseObject):
        pass


    @classmethod
    def commit(cls):

        cls.insertNew()
        cls.updateDirty()
        cls.deleteRemoved()


    @classmethod
    def insertNew(cls):

        for obj in cls.newObjects:
            # objectMapper = MapperRegistry.getMapper(obj.__class__.__name__)
            # objectMapper.insert(obj)
            pass


    @classmethod
    def updateDirty(cls):

        for obj in cls.newObjects:
            # objectMapper = MapperRegistry.getMapper(obj.__class__.__name__)
            # objectMapper.update(obj)
            pass


    @classmethod
    def deleteRemoved(cls):

        for obj in cls.newObjects:
            # objectMapper = MapperRegistry.getMapper(obj.__class__.__name__)
            # objectMapper.remove(obj)
            pass


class Album(PresentedInDatabaseObject):

    def __init__(self, title, artist):
        super().__init__()

        self.title: str = title
        self.artist: str = artist

        self.markNew()

    def setTitle(self, title: str):

        self.title = title
        self.markDirty()


# TODO: Кто создает UnitOfWork