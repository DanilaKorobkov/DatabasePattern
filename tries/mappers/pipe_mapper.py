from tries.mappers.i_mapper import *
# Internal
from tries.domain.pipe import Pipe
# Python
import sqlite3


@mapperFor(Pipe)
class PipeMapper(IMapper):

    def find(self, primaryKey):

        with sqlite3.connect('example.db') as databaseSession:

            dataSets = databaseSession.execute("SELECT * FROM Pipes WHERE Id = ?", (primaryKey, ))
            return self.handleDataSets(dataSets)
    

    def handleDataSets(self, dataSets):

        results = []

        for dataSet in dataSets:
            iterator = iter(dataSet)

            session = Pipe()

            session.primaryKey = next(iterator)
            session.start = next(iterator)
            session.stop = next(iterator)

            session.pipes = PipeMapper.find()

            results.append(session)

        return results