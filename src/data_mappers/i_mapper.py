# Internal
# Python
import sqlite3


class IMapper:

    def __init__(self):

        self.alreadyLoaded = {}


    def __abstractFind(self, databaseId: int):

        if databaseId in self.alreadyLoaded:
            return self.alreadyLoaded.get(databaseId)

        with sqlite3.connect('example.db') as connection:

            transaction = connection.cursor()

            result = transaction.execute(self.__getFindStatement(), (databaseId, )).fetchone()
            return result


    def __getFindStatement(self):
        raise NotImplementedError