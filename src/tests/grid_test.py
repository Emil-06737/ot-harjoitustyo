import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(3, 50)

    def test__add_x_updates_the_grid_correctly(self):
        self.grid._add_x(0, 0)
        self.assertEqual(self.grid.grid, [[1,0,0],[0,0,0],[0,0,0]])
