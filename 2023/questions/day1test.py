import unittest
import os

from day1 import calculate_total_sum1, calculate_total_sum2

class TestCalculateTotalSum(unittest.TestCase):
    def test_calculate_total_sum1(self):
        # Assuming you have a test file with known content for testing
        script_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(script_dir)
        relative_path = os.path.join('testInput', 'day1_1.txt')
        test_file_path = os.path.join(parent_dir, relative_path)
        expected_result = 142  # Replace with the expected result for your test case

        result = calculate_total_sum1(test_file_path)

        self.assertEqual(result, expected_result)
        
    def test_calculate_total_sum2(self):
        # Assuming you have a test file with known content for testing
        script_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(script_dir)
        relative_path = os.path.join('testInput', 'day1_1.txt')
        test_file_path = os.path.join(parent_dir, relative_path)
        expected_result = 142  # Replace with the expected result for your test case

        result = calculate_total_sum2(test_file_path)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()