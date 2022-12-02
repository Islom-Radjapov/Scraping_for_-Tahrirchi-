import pandas as pd
from sqlite3 import connect
import os

# This function separates words and removes duplicates
def split_content(x):
    return set(x.split())


"""
    Be careful, if you run this file, the data in "database.db" will be converted to "Data.csv" and your database.db file will be deleted.
"""

conn = connect('database.db')
result = pd.read_sql('SELECT * FROM Data', con=conn)
result['words'] = result.content.apply(split_content)
conn.close()
result.to_csv('Data.csv', index=False)
os.remove("database.db")