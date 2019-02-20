"""Гарантирует, что каждыйобъект будет загружен из базы данных только один раз,
сохраняя загруженный объект в специальной коллекции. При получении запроса
просматривает коллекцию в поисках нужного объекта"""

# Internal
# Python

class AlbumsMap:

    def __init__(self):
        self.albums = {}


    def __contains__(self, key):
        return key in self.albums


    def addAlbum(self, album):
        self.albums[album.id] = album


    def getAlbum(self, key):
        return self.albums.get(key)

