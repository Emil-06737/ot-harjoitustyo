from services.sprites_for_grid import SpritesForGrid
from sprites.empty import Empty
from sprites.letter import Letter
from repositories.statistics_repository import (
    statistics_repository as default_statistics_repository
)


class Grid:
    """Luokka, joka vastaa pelin sovelluslogiikasta.

    Attributes:
        game_over: Totuusarvo, joka kertoo, että onko peli ohi vai ei.
        _statistics_repository: StatisticsRepository-olio.
        _victory_requirement: Voittosuoran pituusvaatimus.
        _players: Pelaajamäärä.
        _size: Ruudukon sivun pituus.
        _cell_size: Solun koko.
        _player_turn: Numero, joka kertoo, että kenen vuoro on seuraavaksi.
        _grid: Taulukko, jossa pidetään kirjaa ristikon nykytilanteesta.
        sprites: Olio, johon on tallennettu spritet.
    """

    def __init__(self, size, cell_size, victory_requirement=5, players=2, \
                 *, statistics_repository=default_statistics_repository):
        """Luokan konstruktori, jolla luodaan uusi peli.

        Args:
            size: Ruudukon sivun pituus.
            cell_size: Solun koko.
            victory_requirement (int, optional): Voittosuoran pituusvaatimus. Defaults to 5.
            players (int, optional): Pelaajamäärä. Defaults to 2.
            statistics_reporitory (optional): StatisticsRepository-olio.
                Defaults to default_statistics_repository.
        """

        self.game_over = None
        self.sprites = None
        self._statistics_repository = statistics_repository
        self._victory_requirement = victory_requirement
        self._players = self._get_corrected_player_amount(players)
        self._size = size
        self._cell_size = cell_size
        self._player_turn = None
        self._grid = None
        self.reset()

    def reset(self):
        """Aloittaa pelin alusta.
        """
        self.game_over = False
        self._player_turn = 0
        self._init_grid()
        self.sprites = SpritesForGrid()
        self._add_empties()
        self._update_all_sprites()

    def add(self, x, y):
        """Lisää merkin ruudukkoon ja tekee muut tämän yhteydessä vaadittavat toimenpiteet.

        Args:
            x: x-koordinaatti lisättävälle merkille
            y: y-koordinaatti lisättävälle merkille
        """
        if self.game_over or x >= self._size or y >= self._size:
            return
        if self._grid[y][x]:
            return
        letter = self._get_current_players_letter()
        self.sprites.letters.add(Letter(letter, x*self._cell_size, y*self._cell_size))
        self._grid[y][x] = letter
        self._update_all_sprites()
        self._advance_turn()
        winning_line = self._get_winning_line(x, y)
        if winning_line:
            self._finish_game(winning_line)

    def get_played_games(self, players=None, size=None):
        return self._statistics_repository.get_game_count(players, size)

    def get_info_of_the_most_common_game_size(self):
        return self._statistics_repository.get_info_of_the_most_common_grid_size()

    def _add_empties(self):
        """Lisää tyhjät spritet tyhjien spritejen ryhmään.
        """
        for y in range(self._size):
            for x in range(self._size):
                self.sprites.empties.add(Empty(x*self._cell_size, y*self._cell_size))

    def _init_grid(self):
        self._grid = []
        for _ in range(self._size):
            self._grid.append(self._size*[0])

    def _update_all_sprites(self):
        """Päivittää kaikkien spritejen ryhmän.
        """
        self.sprites.all_sprites.empty()
        self.sprites.all_sprites.add(
            self.sprites.empties,
            self.sprites.letters,
            self.sprites.reds
        )

    def _get_winning_line(self, x, y):
        winning_line = self._get_winning_vertical_line(x, y)
        if winning_line:
            return winning_line
        winning_line = self._get_winning_horizontal_line(x, y)
        if winning_line:
            return winning_line
        return self._get_winning_diagonal_line(x, y)

    def _get_winning_vertical_line(self, x, y):
        symbol = self._grid[y][x]
        line = [(x, y)]
        for y1 in range(y - 1, -1, -1):
            current_symbol = self._grid[y1][x]
            if current_symbol == symbol:
                line.append((x, y1))
            else:
                break
        for y1 in range(y + 1, self._size):
            current_symbol = self._grid[y1][x]
            if current_symbol == symbol:
                line.append((x, y1))
            else:
                break
        if len(line) >= self._victory_requirement:
            return sorted(line)
        return None

    def _get_winning_horizontal_line(self, x, y):
        symbol = self._grid[y][x]
        line = [(x, y)]
        for x1 in range(x - 1, -1, -1):
            current_symbol = self._grid[y][x1]
            if current_symbol == symbol:
                line.append((x1, y))
            else:
                break
        for x1 in range(x + 1, self._size):
            current_symbol = self._grid[y][x1]
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
        symbol = self._grid[y][x]
        line = [(x, y)]
        for increment in range(1, min(x, y) + 1):
            current_y = y - increment
            current_x = x - increment
            current_symbol = self._grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        for increment in range(1, self._size - max(x, y)):
            current_y = y + increment
            current_x = x + increment
            current_symbol = self._grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        if len(line) >= self._victory_requirement:
            return sorted(line)
        return None

    def _get_winning_ascending_diagonal_line(self, x, y):
        symbol = self._grid[y][x]
        line = [(x, y)]
        for increment in range(1, min(x + 1, self._size - y)):
            current_y = y + increment
            current_x = x - increment
            current_symbol = self._grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        for increment in range(1, min(self._size - x, y + 1)):
            current_y = y - increment
            current_x = x + increment
            current_symbol = self._grid[current_y][current_x]
            if current_symbol == symbol:
                line.append((current_x, current_y))
            else:
                break
        if len(line) >= self._victory_requirement:
            return sorted(line)
        return None

    def _finish_game(self, line):
        symbol = self._grid[line[0][1]][line[0][0]]
        for coordinates in line:
            red_symbol = Letter(
                symbol, coordinates[0] * self._cell_size, coordinates[1] * self._cell_size, "red")
            self.sprites.reds.add(red_symbol)
        self._update_all_sprites()
        self.game_over = True
        self._statistics_repository.add_game(self._players, self._size)

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
        """Palauttaa hyväksyttävän pelaajamäärän, joka on tarvittaessa korjattu.

        Args:
            players: Pelaajamäärä.

        Returns:
            2, 3 tai 4, jos annettu pelaajamäärä on jokin näistä, muulloin 2.
        """
        if players not in [2, 3, 4]:
            return 2
        return players
