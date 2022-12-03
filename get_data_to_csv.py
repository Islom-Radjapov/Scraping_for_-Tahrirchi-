import pandas as pd
from sqlite3 import connect
import os

"""
    Be careful, if you run this file, the data in "database.db" will be converted to "Data.csv" and your database.db file will be deleted.
"""

conn = connect('database.db')
result = pd.read_sql('SELECT * FROM Data', con=conn)
result.to_csv('Data.csv', index=False)
conn.close()
os.remove("database.db")