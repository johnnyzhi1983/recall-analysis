import sqlite3


def init_db():
    con = sqlite3.connect('recall.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tb_recalls (
                    id INTEGER PRIMARY KEY,
                    url TEXT NOT NULL,
                    title TEXT NOT NULL,
                    date TEXT NOT NULL,
                    content TEXT NOT NULL
                    )''')
    con.commit()
    cur.close()
    con.close()
