import unittest
from pe2_library import FibonacciSequence, find_sum

# create a class of test cases that inherits from TestCase
# (we 'subclass' unittest.TestCase)
class TestFibonacciSequenceMethods(unittest.TestCase):

    def test_even_sum(self):
        self.assertEqual(FibonacciSequence().even_sum(), 4613732)

    def test_find_sum(self):
        # It works without an argument
        self.assertEqual(find_sum(), 4613732)
        # It works with an argument
        self.assertEqual(find_sum(35), 44)

if __name__ == '__main__':
    # run the tests with:
    unittest.main()

    # or:
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacciSequenceMethods)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # as well as from the command line:
    # `python3 -m unittest specs.py`
    # `python3 -m unittest specs.TestFibonacciSequenceMethods`
    # `python3 -m unittest specs.TestFibonacciSequenceMethods.test_even_sum`


    # or learn more with the unittest module help:
    # `python -m unittest -h`
