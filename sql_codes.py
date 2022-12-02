import sqlite3

# create databasa and append data
def add_data(url, date, title, content):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS Data (ulr text, date text, title text, content text) ")
        cursor.execute(f"INSERT INTO Data VALUES ('{url}', '{date}', '{title}', '{content}')")
        connect.commit()
        connect.close()

# get the latest information header
def get_last_title():
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        title = cursor.execute(f"SELECT title FROM Data ORDER BY title DESC LIMIT 1; ").fetchone()
        connect.close()
        return title[0]