import unittest
import runner_and_tournament as rat
from pprint import pprint
from runner import Runner

class TestRunner(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_walk(self):
        test_runner = Runner('Ahmed')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_run(self):
        test_runner = Runner('Ahmed')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_challenge(self):
        test_runner_1 = Runner('Ahmed')
        test_runner_2 = Runner('Mahmud')
        for _ in range(10):
            test_runner_1.run()
            test_runner_2.walk()
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)

class TestTournament(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def setUp(self) -> None:
        self.usain = rat.Runner('Usain', 10)
        self.andrei = rat.Runner('Andrei', 9)
        self.nick = rat.Runner('Nick', 3)

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_first_tournament(self) -> None:
        tournament = rat.Tournament(90, self.nick, self.usain)
        TestTournament.all_results = tournament.start()
        last_runner_name = TestTournament.all_results[max(TestTournament.all_results.keys())][0].name
        self.assertEqual(last_runner_name, 'Nick')

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_second_tournament(self) -> None:
        tournament = rat.Tournament(90, self.nick, self.andrei)
        TestTournament.all_results = tournament.start()
        last_runner_name = TestTournament.all_results[max(TestTournament.all_results.keys())][0].name
        self.assertEqual(last_runner_name, 'Nick')

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_third_tournament(self) -> None:
        tournament = rat.Tournament(90, self.nick, self.andrei, self.usain)
        TestTournament.all_results = tournament.start()
        last_runner_name = TestTournament.all_results[max(TestTournament.all_results.keys())][0].name
        self.assertEqual(last_runner_name, 'Nick')

    @classmethod
    def tearDownClass(cls) -> None:
        pprint(cls.all_results)

if __name__ == '__main__':
    unittest.main()