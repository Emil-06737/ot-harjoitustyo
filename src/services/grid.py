from repositories.finished_game_repository import (
    finished_game_repository as default_finished_game_repository
)


class Grid:
    """Luokka, joka vastaa pelin sovelluslogiikasta.

    Attributes:
        grid: Taulukko, jossa pidetään kirjaa ristikon nykytilanteesta.
        game_over: Totuusarvo, joka kertoo, että onko peli ohi vai ei.
        size: Ruudukon sivun pituus.
        _statistics_repository: StatisticsRepository-olio.
        _players: Pelaajamäärä.
        _victory_requirement: Voittosuoran pituusvaatimus.
        _player_turn: Numero, joka kertoo, että kenen vuoro on seuraavaksi.
    """

    def __init__(self, size: int, victory_requirement=5, players=2, \
                 *, finished_game_repository=default_finished_game_repository):
        """Luokan konstruktori, jolla luodaan uusi peli.

        Args:
            size: Ruudukon sivun pituus.
            victory_requirement (int, optional): Voittosuoran pituusvaatimus. Defaults to 5.
            players (int, optional): Pelaajamäärä. Defaults to 2.
            statistics_reporitory (optional): StatisticsRepository-olio.
                Defaults to default_statistics_repository.
        """

        self.grid = None
        self.game_over = None
        self.size = self._get_corrected_size(size)
        self._finished_game_repository = finished_game_repository
        self._players = self._get_corrected_player_amount(players)
        self._victory_requirement = self._get_corrected_victory_requirement(victory_requirement,
                                                                            self.size)
        self._player_turn = None
        self.reset()

    def reset(self):
        """Aloittaa pelin alusta.
        """
        self.game_over = False
        self._player_turn = 0
        self._init_grid()

    def add(self, x, y):
        """Lisää merkin ruudukkoon, jos sallittua,
        ja tekee muut tämän yhteydessä vaadittavat toimenpiteet.

        Args:
            x: x-koordinaatti lisättävälle merkille
            y: y-koordinaatti lisättävälle merkille
        """
        if self.game_over or x >= self.size or y >= self.size:
            return
        if self.grid[y][x]:
            return
        letter = self._get_current_players_letter()
        self.grid[y][x] = letter
        self._advance_turn()
        winning_line = self._get_winning_line(x, y)
        if winning_line:
            self._finish_game(winning_line)

    def get_played_games(self, players=None, size=None):
        return self._finished_game_repository.get_game_count(players, size)

    def get_info_of_the_most_common_game_size(self):
        return self._finished_game_repository.get_info_of_the_most_common_grid_size()

    def _init_grid(self):
        self.grid = []
        for _ in range(self.size):
            self.grid.append(self.size*[0])

    def _get_winning_line(self, x, y):
        winning_line = self._get_winning_vertical_line(x, y)
        if winning_line:
            return winning_line
        winning_line = self._get_winning_horizontal_line(x, y)
        if winning_line:
            return winning_line
        return self._get_winning_diagonal_line(x, y)

    def _get_winning_vertical_line(self, x, y):
        symbol = self.grid[y][x]
        line = [(x, y)]
        for y1 in range(y - 1, -1, -1):
            current_symbol = self.grid[y1][x]
            if current_symbol == symbol:
                line.append((x, y1))
            else:
                break
        for y1 in range(y + 1, self.size):
            current_symbol = self.grid[y1][x]
            if current_symbol == symbol:
                line.append((x, y1))
            else:
                break
        if len(line) >= self._victory_requirement:
            return sorted(line)
        return None

    def _get_winning_horizontal_line(self, x, y):
        symbol = self.grid[y][x]
        line = [(x, y)]
        for x1 in range(x - 1, -1, -1):
            current_symbol = self.grid[y][x1]
            if current_symbol == symbol:
                line.append((x1, y))
            else:
                break
        for x1 in range(x + 1, self.size):
            current_symbol = self.grid[y][x1]
            if current_symbol == symbol:
                line.append((x1, y))
            else:
                break
        if len(line) >= self._victory_requirement:
            return sorted(line)
        return None

    def _get_winning_diagonal_line(self, x, y):
        winning_line = self._get_winning_descending_diagonal_line(x, y)
        if winning_line:
            return winning_line
        return self._get_winning_ascending_diagonal_line(x, y)

    def _get_winning_descending_diagonal_line(self, x, y):
        symbol = self.grid[y][x]
        line = [(x, y)]
        for increment in range(1, min(x, y) + 1):
            current_y = y - increment
            current_x = x - increment
            current_symbol = self.grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        for increment in range(1, self.size - max(x, y)):
            current_y = y + increment
            current_x = x + increment
            current_symbol = self.grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        if len(line) >= self._victory_requirement:
            return sorted(line)
        return None

    def _get_winning_ascending_diagonal_line(self, x, y):
        symbol = self.grid[y][x]
        line = [(x, y)]
        for increment in range(1, min(x + 1, self.size - y)):
            current_y = y + increment
            current_x = x - increment
            current_symbol = self.grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        for increment in range(1, min(self.size - x, y + 1)):
            current_y = y - increment
            current_x = x + increment
            current_symbol = self.grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        if len(line) >= self._victory_requirement:
            return sorted(line)
        return None

    def _finish_game(self, line):
        symbol = self.grid[line[0][1]][line[0][0]]
        for coordinates in line:
            self.grid[coordinates[1]][coordinates[0]] = "r" + symbol
        self.game_over = True
        self._finished_game_repository.add_game(self._players, self.size)

    def _advance_turn(self):
        """Siirtää vuoron seuraavalle pelaajalle.
        """
        self._player_turn = (self._player_turn + 1) % self._players

    def _get_current_players_letter(self):
        """Palauttaa sen pelaajan merkin, jonka vuoro on tällä hetkellä.

        Returns:
            "x", "o", "y" tai "z" riippuen siitä, kenen vuoro on.
        """
        if self._player_turn == 0:
            return "x"
        if self._player_turn == 1:
            return "o"
        if self._player_turn == 2:
            return "y"
        return "z"

    def _get_corrected_player_amount(self, players):
        players = max(players, 2)
        return min(players, 4)

    def _get_corrected_size(self, size):
        size = max(size, 3)
        return min(size, 86)

    def _get_corrected_victory_requirement(self, victory_requirement, grid_size):
        victory_requirement = max(victory_requirement, 3)
        victory_requirement = min(victory_requirement, 10)
        return min(victory_requirement, grid_size)
