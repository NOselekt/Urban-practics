import logging
logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='UTF-8',
                        format="%(levelname)s | %(message)s | %(asctime)s")
import unittest
from rt_with_exceptions import Runner


class TestRunner(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('\"test_walk\" выполнен успешно')
            test_runner = Runner('Ahmed', speed=-1)
            for _ in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)

        except ValueError:
            logging.warning('Неверная скорость для Runner' ,exc_info=True)

    def test_run(self):
        try:
            logging.info('\"test_run\" выполнен успешно')
            test_runner = Runner(name=True)
            for _ in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)

        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        test_runner_1 = Runner('Ahmed')
        test_runner_2 = Runner('Mahmud')
        for _ in range(10):
            test_runner_1.run()
            test_runner_2.walk()
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


if __name__ == '__main__':

    unittest.main()
