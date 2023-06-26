
import sqlite3



def save_timer_message(user_id, start_time, message, timer, number_of_message, reply_markup, image = None):
    conn = sqlite3.connect('timer.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS timers
                 (id INTEGER PRIMARY KEY,
                 user_id TEXT, 
                 start_time REAL, 
                 message TEXT, 
                 timer REAL,
                 number_of_message INTEGER,
                 reply_markup TEXT,
                 image TEXT)''')
    conn.commit()
    c.close()
    conn.close()
    conn = sqlite3.connect('timer.db')
    c = conn.cursor()
    c.execute("INSERT INTO timers VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (None, user_id, start_time, message, timer, number_of_message, reply_markup, image))
    conn.commit()
    c.close()
    conn.close()


def delete_timer_message(user_id, number_of_message):
    conn = sqlite3.connect('timer.db')
    c = conn.cursor()
    c.execute("SELECT * FROM timers WHERE user_id=? AND number_of_message=?", (user_id, number_of_message))
    row = c.fetchone()
    print("Delete row: ", row)
    if row:
        c.execute("DELETE FROM timers WHERE id=?", (row[0],))
        conn.commit()
        c.close()
        conn.close()


def restore_messages_from_db():
    conn = sqlite3.connect('timer.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS timers
                 (id INTEGER PRIMARY KEY,
                 user_id TEXT, 
                 start_time REAL, 
                 message TEXT, 
                 timer REAL,
                 number_of_message INTEGER,
                 reply_markup TEXT,
                 image text)''')
    conn.commit()
    c.execute("SELECT * FROM timers")
    rows = c.fetchall()
    c.close()
    conn.close()
    return rows

