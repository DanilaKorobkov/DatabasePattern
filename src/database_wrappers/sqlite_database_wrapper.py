from .i_database_wrapper import *
# Python
import sqlite3


class SQLiteDatabaseWrapper(IDatabaseWrapper):

    def select(self, databaseTableName: str, primaryKey: int):

        with sqlite3.connect('example.db') as connection:

            transaction = connection.cursor()

            result = transaction.execute('SELECT FROM ? WHERE ID == ?', (databaseTableName, primaryKey))
            return result