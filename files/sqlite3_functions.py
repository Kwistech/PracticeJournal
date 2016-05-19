from datetime import date
from sqlite3 import connect, OperationalError


def create_conn():
    conn = connect("./files/journal.db")
    return conn


def create_db(conn):
    sql = 'CREATE TABLE journal (key PRIMARY KEY, date, ' \
          'practiced, notes, rating)'

    try:
        conn.execute(sql)
    except OperationalError:
        pass


def get_key(conn):
    sql = 'SELECT * FROM journal'

    try:
        results = conn.execute(sql)
    except OperationalError:
        raise
    else:
        entries = results.fetchall()
        return len(entries)


def insert_db(conn, key, p_text, n_text, r_spinbox):
    sql = 'INSERT INTO journal VALUES ("{}", "{}", "{}", "{}", "{}")'
    sql = sql.format(key, date.today(), p_text, n_text, r_spinbox)

    try:
        conn.execute(sql)
    except OperationalError:
        raise
    else:
        print("Successfully added entry into db!")
    finally:
        conn.commit()


def get_db(conn, key):
    sql = 'SELECT * FROM journal WHERE key="{}"'
    sql = sql.format(key)

    try:
        results = conn.execute(sql)
    except OperationalError:
        raise
    else:
        entries = results.fetchall()
        return entries
