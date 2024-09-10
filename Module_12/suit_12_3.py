import unittest
import tests_12_3

suit = unittest.TestSuite()
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TestRunner))
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TestTournament))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suit)