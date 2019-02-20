from src.identity_map import *
# Python
import pytest


@pytest.fixture
def emptyIdentityMap():

    identityMap = IdentityMap()
    return identityMap


@pytest.fixture
def testObject():

    class Object:
        pass

    obj = Object()
    obj.primaryKey = 1

    return obj


def test_get_ifNoObjectWithThisKey_returnNone(emptyIdentityMap):

    nonExistentPrimaryKey= '0'

    obj = emptyIdentityMap.get(nonExistentPrimaryKey)

    assert obj is None


def test_put_storeObjectByThisId(emptyIdentityMap, testObject):

    emptyIdentityMap.put(testObject)

    assert emptyIdentityMap.get(testObject.primaryKey) is testObject


def test_put_ifObjectWithThisKeyAlreadyExists_raiseException(emptyIdentityMap, testObject):

    emptyIdentityMap.put(testObject)

    with pytest.raises(AlreadyExistsError):
        emptyIdentityMap.put(testObject)





