import unittest
from program_logic.grid import Grid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(3, 3)

    def test__grid_is_correct_after_playing_a_game_and_trying_to_add_an_extra_symbol(self):
        self.grid.add(0, 0)
        self.grid.add(0, 1)
        self.grid.add(1, 0)
        self.grid.add(1, 1)
        self.grid.add(2, 0)
        self.grid.add(2, 1)
        self.assertEqual(self.grid.grid, [["rx", "rx", "rx"], ["o", "o", 0], [0, 0, 0]])

    def test__grid_is_correct_after_playing_a_big_game_and_trying_to_add_an_extra_symbol(self):
        self.grid = Grid(10, 5)
        self.grid.add(0, 0)
        self.grid.add(1, 0)
        self.grid.add(0, 1)
        self.grid.add(1, 1)
        self.grid.add(0, 2)
        self.grid.add(1, 2)
        self.grid.add(0, 3)
        self.grid.add(1, 3)
        self.grid.add(0, 4)
        self.grid.add(1, 4)
        self.assertEqual(self.grid.grid, [["rx", "o", 0, 0, 0, 0, 0, 0, 0, 0],
                         ["rx", "o", 0, 0, 0, 0, 0, 0, 0, 0],
                         ["rx", "o", 0, 0, 0, 0, 0, 0, 0, 0],
                         ["rx", "o", 0, 0, 0, 0, 0, 0, 0, 0],
                         ["rx", 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    def test_add_updates_the_grid_correctly(self):
        self.grid.add(0, 0)
        self.assertEqual(self.grid.grid, [["x", 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_add_updates_the_grid_correctly_with_four_players(self):
        self.grid = Grid(4, 4, 4)
        self.grid.add(0, 0)
        self.grid.add(1, 0)
        self.grid.add(2, 0)
        self.grid.add(3, 0)
        self.grid.add(0, 1)
        self.assertEqual(self.grid.grid, [["x", "o", "y", "z"],
                                          ["x", 0, 0, 0],
                                          [0, 0, 0, 0],
                                          [0, 0, 0, 0]])

    def test__get_winning_vertical_line_returns_the_correct_winning_line(self):
        self.grid.grid = [["x", "o", 0],
                           ["x", "o", 0],
                           ["x", 0, 0]]
        self.assertEqual(self.grid._get_winning_vertical_line(0, 2), [(0, 0), (0, 1), (0, 2)])

    def test__get_winning_vertical_line_returns_None_when_there_is_no_winning_vertical_line(self):
        self.grid.grid = [["x", 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
        self.assertEqual(self.grid._get_winning_vertical_line(0, 0), None)

    def test__get_winning_horizontal_line_returns_the_correct_winning_line(self):
        self.grid.grid = [["o", "o", 0],
                           ["x", "x", "x"],
                           [0, 0, 0]]
        self.assertEqual(self.grid._get_winning_horizontal_line(2, 1), [(0, 1), (1, 1), (2, 1)])

    def test__get_winning_horizontal_line_returns_None_when_there_is_no_winning_horizontal_line(self):
        self.grid.grid = [["x", 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
        self.assertEqual(self.grid._get_winning_horizontal_line(0, 0), None)

    def test__get_winning_descending_diagonal_line_returns_the_correct_winning_line(self):
        self.grid.grid = [["x", 0, 0],
                           ["o", "x", 0],
                           ["o", 0, "x"]]
        self.assertEqual(
            self.grid._get_winning_descending_diagonal_line(0, 0), [(0, 0), (1, 1), (2, 2)])

    def test__get_winning_descending_diagonal_line_returns_None_when_it_should(self):
        self.grid.grid = [["x", 0, 0],
                           ["o", "x", 0],
                           [0, 0, "o"]]
        self.assertEqual(
            self.grid._get_winning_descending_diagonal_line(0, 0), None)

    def test__get_winning_ascending_diagonal_line_returns_the_correct_winning_line(self):
        self.grid.grid = [["o", 0, "x"],
                           ["o", "x", 0],
                           ["x", 0, 0]]
        self.assertEqual(
            self.grid._get_winning_ascending_diagonal_line(2, 0), [(0, 2), (1, 1), (2, 0)])

    def test__get_winning_ascending_diagonal_line_returns_None_when_it_should(self):
        self.grid.grid = [["x", 0, 0],
                           ["o", "x", 0],
                           [0, 0, "x"]]
        self.assertEqual(
            self.grid._get_winning_ascending_diagonal_line(0, 0), None)

    def test_reset_resets__grid(self):
        self.grid.grid = [["o", 0, "rx"],
                           ["o", "rx", 0],
                           ["rx", 0, 0]]
        self.grid.reset()
        self.assertEqual(self.grid.grid, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
