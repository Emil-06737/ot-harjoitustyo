import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(3, 50)

    def test__add_x_updates_the_grid_correctly(self):
        self.grid._add_x(0, 0)
        self.assertEqual(self.grid.grid, [[1,0,0],[0,0,0],[0,0,0]])

    def test__unnormalize_unnormalizes_correctly(self):
        result = self.grid._unnormalize(121, 152)
        self.assertEqual(result, (2, 3))

    def test__check_vertical_victory_recognizes_vertical_victory(self):
        self.grid.grid = [[1, 2, 0],
                          [1, 2, 0],
                          [1, 0, 0]]
        self.assertEqual(self.grid._check_vertical_victory(), True)

    def test__check_vertical_victory_returns_False_when_there_is_no_vertical_victory(self):
        self.grid.grid = [[1, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
        self.assertEqual(self.grid._check_vertical_victory(), False)

    def test__check_horizontal_victory_recognizes_horizontal_victory(self):
        self.grid.grid = [[2, 2, 0],
                          [1, 1, 1],
                          [0, 0, 0]]
        self.assertEqual(self.grid._check_horizontal_victory(), True)

    def test__check_horizontal_victory_returns_False_when_there_is_no_horizontal_victory(self):
        self.grid.grid = [[1, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
        self.assertEqual(self.grid._check_horizontal_victory(), False)

    def test__check_descending_diagonal_victory_recognizes_descending_diagonal_victory(self):
        self.grid.grid = [[1, 0, 0],
                          [2, 1, 0],
                          [2, 0, 1]]
        self.assertEqual(self.grid._check_descending_diagonal_victory(), True)

    def test__check_descending_diagonal_victory_return_False_when_there_is_no_descending_diagonal_victory(self):
        self.grid.grid = [[1, 0, 0],
                          [2, 1, 0],
                          [0, 0, 2]]
        self.assertEqual(self.grid._check_descending_diagonal_victory(), False)

    def test__check_ascending_diagonal_victory_recognizes_ascending_diagonal_victory(self):
        self.grid.grid = [[2, 0, 1],
                          [2, 1, 0],
                          [1, 0, 0]]
        self.assertEqual(self.grid._check_ascending_diagonal_victory(), True)

    def test__check_ascending_diagonal_victory_return_False_when_there_is_no_ascending_diagonal_victory(self):
        self.grid.grid = [[1, 0, 0],
                          [2, 1, 0],
                          [0, 0, 2]]
        self.assertEqual(self.grid._check_ascending_diagonal_victory(), False)
