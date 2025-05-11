from connection_of_db import get_db_connection


class FinishedGameRepository:
    """Tilastojen tallentamisesta vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Connect-olio
        """
        self._connection = connection

    def add_game(self, players, size):
        """Lisää loppuun pelatun pelin tiedot.

        Args:
            players: pelaajien määrä
            size: pelin koko
        """
        cursor = self._connection.cursor()
        sql = "INSERT INTO finished_games (players, size) VALUES (:players, :size)"
        cursor.execute(sql, {"players": players, "size": size})
        self._connection.commit()

    def get_game_count(self, players=None, size=None):
        """Palauttaa pelattujen pelien määrän halutuilla ehdoilla.

        Args:
            players (optional): Pelaajamäärä. Defaults to None.
            size (optional): Ruudukon koko. Defaults to None.

        Returns:
            int: Pelattujen pelien määrä halutuilla ehdoilla.
        """
        players = players or "%"
        size = size or "%"
        sql = "SELECT COUNT(*) FROM finished_games WHERE players LIKE :players AND size LIKE :size"
        cursor = self._connection.cursor()
        result = cursor.execute(sql, {"players":players, "size":size}).fetchone()[0]
        return result

    def get_info_of_the_most_common_grid_size(self):
        """Palauttaa pelatuimman pelikoon tiedot.

        Returns:
            tuple: Ensimmäisessä alkiossa pelatuin koko ja toisessa tämän koon pelien määrä,
                jos tietokannassa on ainakin yksi peli, muulloin palauttaa (None, None).
        """

        sql = "SELECT size, COUNT(*) c FROM finished_games GROUP BY size ORDER BY c desc"
        cursor = self._connection.cursor()
        result = cursor.execute(sql).fetchone()
        if result is None:
            return None, None
        return (result[0], result[1])

    def delete_all(self):
        """Poistaa tietokannan sisällön.
        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM finished_games")
        self._connection.commit()


finished_game_repository = FinishedGameRepository(get_db_connection())
