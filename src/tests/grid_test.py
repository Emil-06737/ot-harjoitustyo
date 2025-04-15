import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(3, 50, 3)

    def test__add_x_updates_the_grid_correctly(self):
        self.grid._add_x(0, 0)
        self.assertEqual(self.grid._grid, [["x",0,0],[0,0,0],[0,0,0]])

    def test__check_vertical_victory_recognizes_vertical_victory(self):
        self.grid._grid = [["x", "o", 0],
                          ["x", "o", 0],
                          ["x", 0, 0]]
        self.assertEqual(self.grid._check_vertical_victory(0, 2), True)

    def test__check_vertical_victory_returns_False_when_there_is_no_vertical_victory(self):
        self.grid._grid = [["x", 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
        self.assertEqual(self.grid._check_vertical_victory(0, 0), False)

    def test__check_horizontal_victory_recognizes_horizontal_victory(self):
        self.grid._grid = [["o", "o", 0],
                          ["x", "x", "x"],
                          [0, 0, 0]]
        self.assertEqual(self.grid._check_horizontal_victory(2, 1), True)

    def test__check_horizontal_victory_returns_False_when_there_is_no_horizontal_victory(self):
        self.grid._grid = [["x", 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
        self.assertEqual(self.grid._check_horizontal_victory(0, 0), False)

    def test__check_descending_diagonal_victory_recognizes_descending_diagonal_victory(self):
        self.grid._grid = [["x", 0, 0],
                          ["o", "x", 0],
                          ["o", 0, "x"]]
        self.assertEqual(self.grid._check_descending_diagonal_victory(0, 0), True)

    def test__check_descending_diagonal_victory_return_False_when_there_is_no_descending_diagonal_victory(self):
        self.grid._grid = [["x", 0, 0],
                          ["o", "x", 0],
                          [0, 0, "o"]]
        self.assertEqual(self.grid._check_descending_diagonal_victory(0, 0), False)

    def test__check_ascending_diagonal_victory_recognizes_ascending_diagonal_victory(self):
        self.grid._grid = [["o", 0, "x"],
                          ["o", "x", 0],
                          ["x", 0, 0]]
        self.assertEqual(self.grid._check_ascending_diagonal_victory(2, 0), True)

    def test__check_ascending_diagonal_victory_return_False_when_there_is_no_ascending_diagonal_victory(self):
        self.grid._grid = [["x", 0, 0],
                          ["o", "x", 0],
                          [0, 0, "x"]]
        self.assertEqual(self.grid._check_ascending_diagonal_victory(0, 0), False)
