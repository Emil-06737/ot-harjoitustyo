import sqlite3
from configuration import PATH_OF_DATABASE_FILE

connection = sqlite3.connect(PATH_OF_DATABASE_FILE)
connection.row_factory = sqlite3.Row


def get_db_connection():
    return connection
