import sqlite3
def insert_to_db(values:list):
    conn = sqlite3.connect('sqlite.db')
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO auction (date, place, status, deadline, payment, organizator) VALUES (?, ?, ?, ?, ?, ?)", values)
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('sqlite.db')
    cursor = conn.cursor()
    cursor.execute(
        "Delete from auction")
    conn.commit()
    conn.close()