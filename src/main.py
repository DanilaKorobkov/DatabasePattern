from src.data_mappers.vehicle_mapper import *
from src.identity_map import IdentityMap
from src.database_wrappers.sqlite_database_wrapper import SQLiteDatabaseWrapper
# Python
import sqlite3

connection = sqlite3.connect('example.db')
connection.execute('CREATE TABLE IF NOT EXISTS Vehicle (Id INTEGER PRIMARY KEY AUTOINCREMENT, Manufacturer TEXT)')
connection.commit()
connection.close()

mapper = VehicleMapper(IdentityMap(), SQLiteDatabaseWrapper())
data = mapper.find(1)
print(data)