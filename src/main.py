# Python
from src.data_mappers.vehicle_mapper import *


if __name__ == '__main__':

    c = VehicleMapper().findById(1)
    print(c)
    # connection = sqlite3.connect('example.db')
    # connection.execute('CREATE TABLE IF NOT EXISTS Vehicle (Id INTEGER PRIMARY KEY AUTOINCREMENT, Manufacturer TEXT)')
    # transaction = connection.cursor()
    # transaction.execute('INSERT INTO Vehicle (Manufacturer) VALUES (?)', ('35',))
    # connection.commit()