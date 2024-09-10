import unittest
from runner import Runner


class TestRunner(unittest.TestCase):
    
    def test_walk(self):
        test_runner = Runner('Ahmed')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = Runner('Ahmed')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_runner_1 = Runner('Ahmed')
        test_runner_2 = Runner('Mahmud')
        for _ in range(10):
            test_runner_1.run()
            test_runner_2.walk()
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)

if __name__ == '__main__':
    unittest.main()