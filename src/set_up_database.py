from connection_of_db import get_db_connection


def set_up_database():
    """Asettaa tietokannan alkutilan.
    """
    connection = get_db_connection()
    remove_tables(connection)
    make_tables(connection)


def remove_tables(connection):
    """Poistaa kaikki tietokantataulut.

    Args:
        connection: Connection-olio
    """
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS finished_games;")
    connection.commit()


def make_tables(connection):
    """Tekee kaikki tietokantataulut.

    Args:
        connection: Connection-olio
    """
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE finished_games (players INT, size INT);")
    connection.commit()
