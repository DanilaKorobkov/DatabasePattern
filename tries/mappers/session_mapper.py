from tries.mappers.i_mapper import *
# Internal
from tries.domain.session import Session
from tries.mappers.pipe_mapper import PipeMapper
# Python
import sqlite3


@mapperFor(Session)
class SessionMapper(IMapper):

    def find(self, primaryKey):

        with sqlite3.connect('example.db') as databaseSession:

            dataSets = databaseSession.execute("SELECT * FROM Sessions WHERE Id = ?", (primaryKey, ))
            return self.handleDataSets(dataSets)

    def handleDataSets(self, dataSets):

        results = []

        for dataSet in dataSets:
            iterator = iter(dataSet)

            session = Session()

            session.primaryKey = next(iterator)
            session.start = next(iterator)
            session.stop = next(iterator)

            session.pipes = PipeMapper.find()

            results.append(session)

        return results
