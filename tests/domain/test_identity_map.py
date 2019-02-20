from src.identity_map import *
# Python
import pytest


class TestIdentityMap:

    @pytest.fixture
    def emptyIdentityMap(self):

        identityMap = IdentityMap()
        return identityMap

    @pytest.fixture
    def testObject(self):

        class Object:
            pass

        obj = Object()
        obj.primaryKey = 1

        return obj


    def test_get_ifNoObjectWithThisKey_returnNone(self, emptyIdentityMap):

        nonExistentPrimaryKey= '0'

        obj = emptyIdentityMap.get(nonExistentPrimaryKey)

        assert obj is None


    def test_put_storeObjectByThisId(self, emptyIdentityMap, testObject):

        emptyIdentityMap.put(testObject)

        assert emptyIdentityMap.get(testObject.primaryKey) is testObject


    def test_put_ifObjectWithThisKeyAlreadyExists_raiseException(self, emptyIdentityMap, testObject):

        emptyIdentityMap.put(testObject)

        with pytest.raises(AlreadyExistsError):
            emptyIdentityMap.put(testObject)