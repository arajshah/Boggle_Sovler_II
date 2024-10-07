import unittest
from boggle_solver import find_all_solutions

def lowercase_string_array(string_array):
    """Lowercases a list of strings in-place."""
    for i in range(len(string_array)):
        string_array[i] = string_array[i].lower()

class TestBoggleSolver(unittest.TestCase):

    # Test case 1: Normal input case
    def test_normal_input(self):
        grid = [['t', 'w', 'y', 'r'],
                ['e', 'n', 'p', 'h'],
                ['g', 'z', 'qu', 'r'],
                ['o', 'n', 't', 'a']]
        dictionary = ['art', 'ego', 'gent', 'get', 'net', 'new', 'newt', 'prat',
                      'pry', 'qua', 'quart', 'quartz', 'rat', 'tar', 'tarp',
                      'ten', 'went', 'wet', 'arty', 'egg', 'not', 'quar']
        expected = ['art', 'ego', 'gent', 'get', 'net', 'new', 'newt', 'prat',
                    'pry', 'qua', 'quar', 'quart', 'quartz', 'rat', 'tar',
                    'tarp', 'ten', 'went', 'wet']

        solutions = find_all_solutions(grid, dictionary)

        lowercase_string_array(solutions)
        lowercase_string_array(expected)
        self.assertEqual(sorted(solutions), sorted(expected))

    # Test case 2: Problem constraint handling (Qu and multi-character sequences)
    def test_problem_constraints(self):
        grid = [['t', 'r', 'e', 'e'],
                ['a', 'st', 'o', 'qu'],
                ['s', 'm', 't', 'n'],
                ['p', 'l', 'a', 'y']]
        dictionary = ['stone', 'queen', 'stoque']
        expected = ['stone', 'queen', 'stoque']

        solutions = find_all_solutions(grid, dictionary)

        lowercase_string_array(solutions)
        lowercase_string_array(expected)
        self.assertEqual(sorted(solutions), sorted(expected))

    # Test case 3: Edge cases (empty dictionary, empty grid, no valid words)
    def test_empty_dictionary(self):
        grid = [['a', 'b', 'c', 'd'],
                ['e', 'f', 'g', 'h'],
                ['i', 'j', 'k', 'l'],
                ['m', 'n', 'o', 'p']]
        dictionary = []
        expected = []

        solutions = find_all_solutions(grid, dictionary)

        lowercase_string_array(solutions)
        lowercase_string_array(expected)
        self.assertEqual(sorted(solutions), sorted(expected))

    def test_empty_grid(self):
        grid = [[]]
        dictionary = ['test']
        expected = []

        solutions = find_all_solutions(grid, dictionary)

        lowercase_string_array(solutions)
        lowercase_string_array(expected)
        self.assertEqual(sorted(solutions), sorted(expected))

    def test_no_valid_words(self):
        grid = [['x', 'y', 'z', 'w'],
                ['q', 'r', 's', 't'],
                ['u', 'v', 'm', 'n'],
                ['o', 'p', 'l', 'k']]
        dictionary = ['apple', 'orange', 'banana']
        expected = []

        solutions = find_all_solutions(grid, dictionary)

        lowercase_string_array(solutions)
        lowercase_string_array(expected)
        self.assertEqual(sorted(solutions), sorted(expected))


if __name__ == '__main__':
    unittest.main()
