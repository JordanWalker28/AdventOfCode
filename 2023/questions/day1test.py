import unittest
import os

from day1 import *

class TestCalculateTotalSum(unittest.TestCase):
    def setup_file_path(self, file):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(script_dir)
        relative_path = os.path.join('testInput', file)
        test_file_path = os.path.join(parent_dir, relative_path)
        return test_file_path
    
    def test_calculate_total_sum1(self):
        test_file_path = self.setup_file_path('day1_1.txt')
        result = calculate_total_sum1(test_file_path)
        self.assertEqual(result, 142)

    def test_calculate_total_sum2(self):
        test_file_path = self.setup_file_path('day1_2.txt')
        result = calculate_total_sum2(test_file_path)
        self.assertEqual(result, 281)
        
    def test_get_first_and_last_digits_case1(self):
        result = get_first_and_last_digits("7pqrstsixteen")
        self.assertEqual(result, 76)

    def test_get_first_and_last_digits_case2(self):
        result = get_first_and_last_digits("13abc45")
        self.assertEqual(result, 15)

    def test_get_first_and_last_digits_case3(self):
        result = get_first_and_last_digits("42xyz")
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()