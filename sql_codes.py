import sqlite3

# create databasa and append data
def add_data(url, date, title, content, words, count_words):
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS Data (ulr text, date text, title text, content text, words text, count_words integer) ")
        cursor.execute(f"INSERT INTO Data VALUES ('{url}', '{date}', '{title}', '{content}', '{words}', '{count_words}')")
        connect.commit()
        connect.close()