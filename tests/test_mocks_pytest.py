# Internal
# Python
import pytest, pytest_mock
# Mocks

class AlbumsMap:

    def __init__(self):
        self.albums = {}


    def __contains__(self, key):
        return key in self.albums


    def addAlbum(self, album):
        self.albums[album.id] = album


    def getAlbum(self, key):
        return self.albums.get(key)



def test_add_addItem():

    assert
