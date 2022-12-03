import sqlite3

# create database
def create_db():
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS "Data" (
                                    "id"	INTEGER NOT NULL UNIQUE,
                                    "url"	TEXT,
                                    "date"	TEXT,
                                    "title"	TEXT,
                                    "content"	TEXT,
                                    PRIMARY KEY("id" AUTOINCREMENT)
                                );""")
        connect.commit()
        connect.close()

# append data
def add_data(url, date, title, content):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO Data (url, date, title, content) VALUES ('{url}', '{date}', '{title}', '{content}')")
        connect.commit()
        connect.close()

# get the latest information header
def get_last_title():
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        title = cursor.execute(f"SELECT title FROM Data ORDER BY id DESC LIMIT 1").fetchone()
        cursor.close()
        connect.close()
        return title[0]