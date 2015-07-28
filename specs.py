import unittest
from pe2_library import FibonacciSequence, find_sum

# create a class of test cases that inherits from TestCase
# (we 'subclass' unittest.TestCase)
class TestFibonacciSequenceMethods(unittest.TestCase):

    def test_even_sum(self):
        self.assertEqual(FibonacciSequence().even_sum(), 4613732)

    def test_find_sum(self):
        self.assertEqual(find_sum(), 4613732)

if __name__ == '__main__':
    unittest.main()
