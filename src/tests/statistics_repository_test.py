import unittest
from repositories.statistics_repository import statistics_repository

class TestStatisticsRepository(unittest.TestCase):
    def setUp(self):
        statistics_repository.delete_all()
        statistics_repository.add_game(2, 13)
        statistics_repository.add_game(3, 13)
        statistics_repository.add_game(2, 10)

    def test_add_game_adds_games(self):
        self.assertEqual(statistics_repository.get_game_count(), 3)

    def test_delete_all_deletes_all_games(self):
        statistics_repository.delete_all()
        self.assertEqual(statistics_repository.get_game_count(), 0)

    def test_get_info_of_the_most_common_grid_size_returns_the_correct_info(self):
        info = statistics_repository.get_info_of_the_most_common_grid_size()
        self.assertEqual(info, (13, 2))

    def test_get_game_count_with_two_players_returns_the_correct_game_count(self):
        gamecount = statistics_repository.get_game_count(2)
        self.assertEqual(gamecount, 2)
