"""Гарантирует, что каждыйобъект будет загружен из базы данных только один раз,
сохраняя загруженный объект в специальной коллекции. При получении запроса
просматривает коллекцию в поисках нужного объекта"""

# Internal
# Python


class AlreadyExistsError(Exception):
    pass


class IdentityMap:

    def __init__(self):

        self.loadedObjects = {}


    def get(self, primaryKey):

        return self.loadedObjects.get(primaryKey, None)


    def put(self, obj):

        if self.get(obj.primaryKey) is None:
            self.loadedObjects[obj.primaryKey] = obj

        else:
            raise AlreadyExistsError('Try to add object' + str(obj.__dict__) + 'with type ' + str(type(obj)) + ' which already stored')

