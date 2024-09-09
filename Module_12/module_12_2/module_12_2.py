import unittest
import runner_and_tournament as rt
from pprint import pprint


class TestTournament(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results = {}


    def setUp(self) -> None:
        self.usain = rt.Runner('Usain', 10)
        self.andrei = rt.Runner('Andrei', 9)
        self.nick = rt.Runner('Nick', 3)

    def test_tournament(self) -> None:
        tournament = rt.Tournament(90, self.nick, self.andrei, self.usain)
        TestTournament.all_results = tournament.start()
        last_runner_name = TestTournament.all_results[max(TestTournament.all_results.keys())][0].name
        self.assertEqual(last_runner_name, 'Nick')

    @classmethod
    def tearDownClass(cls) -> None:
        pprint(cls.all_results)


if __name__ == '__main__':
    unittest.main()