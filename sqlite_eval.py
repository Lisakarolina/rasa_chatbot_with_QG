
import sqlite3


def insert_data(sensical, informative, compare, sus_1, sus_2, sus_3, sus_4,
                sus_5, sus_6, sus_7, sus_8, sus_9, sus_10):
    connection = sqlite3.connect('eval.db')
    cur = connection.cursor()

    INSERTION = '''INSERT INTO evaluation(sensical, informative, compare, sus_1,
                sus_2, sus_3, sus_4, sus_5, sus_6, sus_7, sus_8, sus_9, sus_10)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    cur.execute('''CREATE TABLE IF NOT EXISTS evaluation
                (sensical INTEGER, informative INTEGER, compare INTEGER, sus_1 INTEGER,
                sus_2 INTEGER, sus_3 INTEGER, sus_4 INTEGER, sus_5 INTEGER, sus_6 INTEGER,
                sus_7 INTEGER, sus_8 INTEGER, sus_9 INTEGER, sus_10 INTEGER)''')

    cur.execute(INSERTION, (sensical, informative, compare, sus_1, sus_2,
                sus_3, sus_4, sus_5, sus_6, sus_7, sus_8, sus_9, sus_10))
    connection.commit()
    connection.close()


def insert_data_qa(q, a):
    connection = sqlite3.connect('eval.db')
    cur = connection.cursor()

    INSERTION = '''INSERT INTO qa(question,answer) VALUES (?, ?)'''

    cur.execute('''CREATE TABLE IF NOT EXISTS qa
                (question TEXT, answer TEXT)''')

    cur.execute(INSERTION, (q, a))
    connection.commit()
    connection.close()
