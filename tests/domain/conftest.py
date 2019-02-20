# Python
import pytest


@pytest.fixture
def testObject():

    class Object:
        pass

    obj = Object()
    obj.primaryKey = 1

    return obj