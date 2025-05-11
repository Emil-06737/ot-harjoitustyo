import unittest
from repositories.finished_game_repository import finished_game_repository

class TestStatisticsRepository(unittest.TestCase):
    def setUp(self):
        finished_game_repository.delete_all()
        finished_game_repository.add_game(2, 13)
        finished_game_repository.add_game(3, 13)
        finished_game_repository.add_game(2, 10)

    def test_add_game_adds_games(self):
        self.assertEqual(finished_game_repository.get_game_count(), 3)

    def test_delete_all_deletes_all_games(self):
        finished_game_repository.delete_all()
        self.assertEqual(finished_game_repository.get_game_count(), 0)

    def test_get_info_of_the_most_common_grid_size_returns_the_correct_info(self):
        info = finished_game_repository.get_info_of_the_most_common_grid_size()
        self.assertEqual(info, (13, 2))

    def test_get_game_count_with_two_players_returns_the_correct_game_count(self):
        gamecount = finished_game_repository.get_game_count(2)
        self.assertEqual(gamecount, 2)
