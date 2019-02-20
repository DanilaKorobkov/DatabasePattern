from .i_mapper import *


class VehicleMapper(IMapper):

    def __getFindStatement(self):

        return 'SELECT * FROM Vehicle WHERE Id == ?'


    def find(self, databaseId):

        return self.__abstractFind(databaseId)

