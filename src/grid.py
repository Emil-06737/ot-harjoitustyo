import pygame
from sprites.empty import Empty
from sprites.letter import Letter


class Grid:
    """Luokka, joka vastaa pelin sovelluslogiikasta.

    Attributes:
        _victory_requirement: Voittosuoran pituusvaatimus.
        _players: Pelaajamäärä.
        game_over: Totuusarvo, joka kertoo, että onko peli ohi vai ei.
        _player_turn: Numero, joka kertoo, että kenen vuoro on seuraavaksi.
        _size: Ruudukon sivun pituus.
        _cell_size: Solun koko.
        _empties: Tyhjien spritejen ryhmä.
        _letters: Kirjain spritejen ryhmä.
        _reds: Punaisten spritejen ryhmä.
        all_sprites: Kaikkien spritejen ryhmä.
        _grid: Taulukko, jossa pidetään kirjaa ristikon nykytilanteesta.
    """

    def __init__(self, size, cell_size, victory_requirement=5, players=2):
        """Luokan konstruktori, jolla luodaan uusi peli.

        Args:
            size: Ruudukon sivun pituus.
            cell_size: Solun koko.
            victory_requirement (int, optional): Voittosuoran pituusvaatimus. Defaults to 5.
            players (int, optional): Pelaajamäärä. Defaults to 2.
        """

        self._victory_requirement = victory_requirement
        self._players = self._get_corrected_player_amount(players)
        self.game_over = False
        self._player_turn = 0
        self._size = size
        self._cell_size = cell_size
        self._empties = pygame.sprite.Group()
        self._letters = pygame.sprite.Group()
        self._reds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._init_grid()
        self._add_empties()
        self._update_all_sprites()

    def add(self, x, y):
        """Lisää merkin ruudukkoon ja tekee muut tämän yhteydessä vaadittavat toimenpiteet.

        Args:
            x: X-koordinaatti lisättävälle merkille
            y: Y-koordinaatti lisättävälle merkille
        """
        if self.game_over or x >= self._size or y >= self._size:
            return
        if self._grid[y][x]:
            return
        letter = self._get_current_players_letter()
        self._letters.add(Letter(letter, x*self._cell_size, y*self._cell_size))
        self._grid[y][x] = letter
        self._update_all_sprites()
        self._advance_turn()
        self._check_victory(x, y)

    def _add_empties(self):
        """Lisää tyhjät spritet tyhjien spritejen ryhmään.
        """
        for y in range(self._size):
            for x in range(self._size):
                self._empties.add(Empty(x*self._cell_size, y*self._cell_size))

    def _init_grid(self):
        """Alustaa taulukon, jossa pidetään kirjaa ristikon nykytilanteesta.
        """
        self._grid = []
        for _ in range(self._size):
            self._grid.append(self._size*[0])

    def _update_all_sprites(self):
        """Päivittää kaikkien spritejen ryhmän.
        """
        self.all_sprites.empty()
        self.all_sprites.add(
            self._empties,
            self._letters,
            self._reds
        )

    def _check_victory(self, x, y):
        """Tarkistaa, että onko peli ohi, ja tekee tarvittavat toimenpiteet, jos näin on.

        Args:
            x: Viimeksi lisätyn merkin x-koordinaatti.
            y: Viimeksi lisätyn merkin y-koordinaatti.
        """
        if self._check_vertical_victory(x, y):
            return
        if self._check_horizontal_victory(x, y):
            return
        self._check_diagonal_victory(x, y)

    def _check_vertical_victory(self, x, y):
        """Tarkistaa, että onko pystysuora voitto tapahtunut,
        ja tekee tarvittavat toimenpiteet, jos näin on.

        Args:
            x: Viimeksi lisätyn merkin x-koordinaatti.
            y: Viimeksi lisätyn merkin y-koordinaatti.

        Returns:
            True, jos pystysuora voitto on tapahtunut, muulloin False.
        """
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
            self._finish_game(line)
            return True
        return False


    def _check_horizontal_victory(self, x, y):
        """Tarkistaa, että onko vaakasuora voitto tapahtunut,
        ja tekee tarvittavat toimenpiteet, jos näin on.

        Args:
            x: Viimeksi lisätyn merkin x-koordinaatti.
            y: Viimeksi lisätyn merkin y-koordinaatti.

        Returns:
            True, jos vaakasuora voitto on tapahtunut, muulloin False.
        """
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
            self._finish_game(line)
            return True
        return False

    def _check_diagonal_victory(self, x, y):
        """Tarkistaa, että onko diagonaalinen voitto tapahtunut,
        ja tekee tarvittavat toimenpiteet, jos näin on.

        Args:
            x: Viimeksi lisätyn merkin x-koordinaatti.
            y: Viimeksi lisätyn merkin y-koordinaatti.

        Returns:
            True, jos diagonaalinen voitto on tapahtunut, muulloin False.
        """
        if self._check_descending_diagonal_victory(x, y):
            return True
        return self._check_ascending_diagonal_victory(x, y)

    def _check_descending_diagonal_victory(self, x, y):
        """Tarkistaa, että onko laskeva diagonaalinen voitto tapahtunut,
        ja tekee tarvittavat toimenpiteet, jos näin on.

        Args:
            x: Viimeksi lisätyn merkin x-koordinaatti.
            y: Viimeksi lisätyn merkin y-koordinaatti.

        Returns:
            True, jos laskeva diagonaalinen voitto on tapahtunut, muulloin False.
        """
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
            self._finish_game(line)
            return True
        return False

    def _check_ascending_diagonal_victory(self, x, y):
        """Tarkistaa, että onko laskeva diagonaalinen voitto tapahtunut,
        ja tekee tarvittavat toimenpiteet, jos näin on.

        Args:
            x: Viimeksi lisätyn merkin x-koordinaatti.
            y: Viimeksi lisätyn merkin y-koordinaatti.

        Returns:
            True, jos nouseva diagonaalinen voitto on tapahtunut, muulloin False.
        """
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
            self._finish_game(line)
            return True
        return False

    def _finish_game(self, line):
        """Tekee tarvittafat toimenpiteet, kun voitto on tapahtunut.

        Args:
            line: Lista, joka koostuu voittosuoran pisteistä,
            jotka ovat tupleja muotoa (x, y),
            jossa x on pisteen x-koordinaatti ja y on pisteen y-koordinaatti.
        """
        symbol = self._grid[line[0][1]][line[0][0]]
        for coordinates in line:
            red_symbol = Letter(
                symbol, coordinates[0] * self._cell_size, coordinates[1] * self._cell_size, "red")
            self._reds.add(red_symbol)
        self._update_all_sprites()
        self.game_over = True

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
