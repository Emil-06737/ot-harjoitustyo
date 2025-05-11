import os
import pygame


class Displayer:
    """Luokka, joka vastaa näytön päivittämisestä.
    """

    def __init__(self, grid, display, cell_size = 50):
        """Luokan konstruktori, joka luo näytön päivittäjän.

        Args:
            grid: Pelin sovelluslogiikasta vastaava luokka.
            display: Näyttö.
        """

        self._grid = grid
        self._display = display
        self._show_info = False
        self._images = self._get_images()
        self._cell_size = cell_size

    def _get_images(self):
        images = {}
        images[0] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "empty.png"))
        images["x"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "black x.png"))
        images["rx"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "red x.png"))
        images["o"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "black o.png"))
        images["ro"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "red o.png"))
        images["y"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "black y.png"))
        images["ry"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "red y.png"))
        images["z"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "black z.png"))
        images["rz"] = pygame.image.load(os.path.join(os.path.dirname(__file__),
                         "..", "assets", "red z.png"))
        return images

    def display(self):
        """Päivittää näytön.
        """

        self._blit_grid()
        if self._show_info:
            self._display_info_with_background()
        pygame.display.update()

    def toggle_info(self):
        """Muuttaa statistiikan näkyvyyttä."""
        if self._show_info:
            self._show_info = False
        else:
            self._show_info = True

    def _blit_grid(self):
        for i in range(self._grid.size):
            for i2 in range(self._grid.size):
                current = self._grid.grid[i][i2]
                self._display.blit(self._images[current], (i2*self._cell_size, i*self._cell_size))

    def _display_info_with_background(self):
        small = True if self._grid.size < 7 else False
        self._blit_info_background(small)
        self._create_info(small)

    def _blit_info_background(self, small):
        if small:
            width, height = 150, 100
        else:
            width, height = 350, 250
        background = pygame.Surface((width, height))
        background.set_alpha(200)
        background.fill((50, 50, 50))
        self._display.blit(background, (0, 0))

    def _create_info(self, small):
        texts = self._get_statistics_texts()
        self._blit_texts(texts, small)

    def _get_statistics_texts(self):
        played_games = self._grid.get_played_games()
        two_player_games = self._grid.get_played_games(2)
        most_common_size, common_size_games = self._grid.get_info_of_the_most_common_game_size()

        texts = []
        texts.append(f"Pelien määrä: {played_games}")
        texts.append(f"Joista kaksinpelejä: {two_player_games}")
        texts.append("")
        texts.append(f"Pelatuin koko: {most_common_size or 'ei mikään'}")
        texts.append(f"Jonka pelimäärä: {common_size_games or 0}")
        return texts

    def _blit_texts(self, texts, small):
        if small:
            font_size = 10
            line_increment = 17
        else:
            font_size = 30
            line_increment = 50
        font = pygame.font.SysFont("Arial", font_size)
        text_color = (0, 255, 0)
        base_x = 10
        base_y = 10

        for i in range(len(texts)):
            text = texts[i]
            rendered_text = font.render(text, True, text_color)
            self._display.blit(rendered_text, (base_x, base_y + i * line_increment))
