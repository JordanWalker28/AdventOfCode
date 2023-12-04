import unittest
import sys
import os
sys.path.append('../questions')

from day3 import *

class TestCalculateTotalSum(unittest.TestCase):
    def setup_file_path(self, file):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(script_dir)
        relative_path = os.path.join('testInput', file)
        test_file_path = os.path.join(parent_dir, relative_path)
        return test_file_path
    
    def test_calculate_total_sum1(self):
        test_file_path = self.setup_file_path('day3_1.txt')
        data = read_input_file(test_file_path)
        G, R, C = parse_input(data)
        result = main(test_file_path)
        self.assertEqual(result, 4361)
        
    def test_calculate_total_sum1(self):
        test_file_path = self.setup_file_path('day3_1.txt')
        data = read_input_file(test_file_path)
        G, R, C = parse_input(data)
        result = main(test_file_path)
        self.assertEqual(result, 467835)

if __name__ == '__main__':
    unittest.main()