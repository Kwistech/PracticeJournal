from datetime import date
from sqlite3 import connect, OperationalError


def create_conn():
    """Create connection to journal.db."""
    conn = connect("./files/journal.db")
    return conn


def create_db(conn):
    """Create table journal in journal.db.

    Args:
        conn (sqlite3.Connection): Connection to journal.db.

    Raises:
        OperationalError: When table already exists; pass.
    """
    sql = 'CREATE TABLE journal (key PRIMARY KEY, date, ' \
          'practiced, notes, rating)'

    try:
        conn.execute(sql)
    except OperationalError:
        pass


def get_key(conn):
    """Get number of entries in database table journal.

    Args:
        conn (sqlite3.Connection): Connection to journal.db.

    Returns:
        int: Number of entries in database table journal.

    Raises:
        OperationalError: When sql statement does not work; raise.
    """
    sql = 'SELECT * FROM journal'

    try:
        results = conn.execute(sql)
    except OperationalError:
        raise
    else:
        entries = results.fetchall()
        return len(entries)


def insert_db(conn, key, p_text, n_text, r_spinbox):
    """Insert user input into database table journal.

    Args:
        conn (sqlite3.Connection): Connection to journal.db.
        key (int): Number of entries in database (zero-based numbering).
        p_text (str): Data from the p_text tkinter Text field.
        n_text (str): Data from the n_text tkinter Text field.
        r_spinbox (str): Data from the r_spinbox tkinter Spinbox.

    Raises:
        OperationalError: When sql statement does not work; raise.
    """
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
    """Get most recent entry in database table journal.

    Args:
        conn (sqlite3.Connection): Connection to journal.db.
        key (int): Number of entry in database.

    Returns:
        list: Contains all entries matching specified sql SELECT statement

    Raises:
        OperationalError: When sql statement does not work; raise.
    """
    sql = 'SELECT * FROM journal WHERE key="{}"'
    sql = sql.format(key)

    try:
        results = conn.execute(sql)
    except OperationalError:
        raise
    else:
        entries = results.fetchall()
        return entries
