import unittest
import os

from day1 import *

class TestCalculateTotalSum(unittest.TestCase):
    def test_calculate_total_sum1(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(script_dir)
        relative_path = os.path.join('testInput', 'day1_1.txt')
        test_file_path = os.path.join(parent_dir, relative_path)
        expected_result = 142  
        result = calculate_total_sum1(test_file_path)
        self.assertEqual(result, expected_result)
    
    def test_calculate_total_sum2(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(script_dir)
        relative_path = os.path.join('testInput', 'day1_2.txt')
        test_file_path = os.path.join(parent_dir, relative_path)
        expected_result = 281  
        result = calculate_total_sum2(test_file_path)
        self.assertEqual(result, expected_result)
        
    def test_get_first_and_last_digits_case1(self):
        expected_result = 76
        result = get_first_and_last_digits("7pqrstsixteen")
        self.assertEqual(result, expected_result)

    def test_get_first_and_last_digits_case2(self):
        expected_result = 15
        result = get_first_and_last_digits("13abc45")
        self.assertEqual(result, expected_result)

    def test_get_first_and_last_digits_case3(self):
        expected_result = 42
        result = get_first_and_last_digits("42xyz")
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()