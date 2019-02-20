

class IMapper:

    def __init__(self, identityMap, databaseWrapper):

        self.identityMap = identityMap
        self.databaseWrapper = databaseWrapper

        self.tableName: str = None


    def add(self, obj):
        raise NotImplementedError

    def update(self, obj):
        raise NotImplementedError

    def remove(self, primaryKey):
        raise NotImplementedError

    def find(self, primaryKey):
        raise NotImplementedError