from src.data_mappers.vehicle_mapper import *
# Internal
from src.identity_map import IdentityMap
from src.database_wrappers.i_database_wrapper import IDatabaseWrapper



def test_find_ifObjectAlreadyLoaded_returnThisObject(mocker, testObject):

    mockIdentityMap = IdentityMap()
    mocker.patch.object(mockIdentityMap, 'get', return_value = testObject)

    mockDatabaseWrapper = IDatabaseWrapper()
    mocker.patch.object(mockDatabaseWrapper, 'select')

    vehicleMapper = VehicleMapper(mockIdentityMap, None)
    obj = vehicleMapper.find(testObject.primaryKey)

    assert obj is testObject
    mockDatabaseWrapper.select.assert_not_called()


def test_find_ifObjectNotLoaded_callDatabaseToSelect(mocker, testObject):

    mockIdentityMap = IdentityMap()
    mocker.patch.object(mockIdentityMap, 'get', return_value = None)

    mockDatabaseWrapper = IDatabaseWrapper()
    mocker.patch.object(mockDatabaseWrapper, 'select')

    vehicleMapper = VehicleMapper(mockIdentityMap, mockDatabaseWrapper)


    vehicleMapper.find(testObject.primaryKey)

    mockDatabaseWrapper.select.assert_called_once_with('Vehicle', testObject.primaryKey)

