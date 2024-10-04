const { findAllSolutions } = require('/home/codio/workspace/Boggle_Testing/boggle_solver.js');

/** Lowercases a string array in-place. (Used for case-insensitive string array
 *  matching).
 * @param {string[]} stringArray - String array to be lowercase.
 */
function lowercaseStringArray(stringArray) {
  for (let i = 0; i < stringArray.length; i++) {
    stringArray[i] = stringArray[i].toLowerCase();
  }
}

describe('Boggle Solver tests suite:', () => {

  // Test case 1: Normal input case
  describe('Normal input', () => {
    test('Finds all valid words in a simple grid', () => {
      const grid = [['t', 'w', 'y', 'r'],
                    ['e', 'n', 'p', 'h'],
                    ['g', 'z', 'qu', 'r'],
                    ['o', 'n', 't', 'a']];
      const dictionary = ['art', 'ego', 'gent', 'get', 'net', 'new', 'newt', 'prat',
                          'pry', 'qua', 'quart', 'quartz', 'rat', 'tar', 'tarp',
                          'ten', 'went', 'wet', 'arty', 'egg', 'not', 'quar'];
      const expected = ['art', 'ego', 'gent', 'get', 'net', 'new', 'newt', 'prat', 'pry', 
                        'qua', 'quar', 'quart', 'quartz', 'rat', 'tar', 'tarp', 'ten', 'went', 'wet'];

      let solutions = findAllSolutions(grid, dictionary);

      lowercaseStringArray(solutions);
      lowercaseStringArray(expected);
      expect(solutions.sort()).toEqual(expected.sort());
    });
  });

  // Test case 2: Problem constraint handling (Qu and multi-character sequences)
  describe('Problem constraints', () => {
    test('Handles multi-character sequences like Qu', () => {
      const grid = [['t', 'r', 'e', 'e'],
                    ['a', 'st', 'o', 'qu'],
                    ['s', 'm', 't', 'n'],
                    ['p', 'l', 'a', 'y']];
      const dictionary = ['stone', 'queen', 'stoque'];
      const expected = ['stone', 'queen', 'stoque'];

      let solutions = findAllSolutions(grid, dictionary);

      lowercaseStringArray(solutions);
      lowercaseStringArray(expected);
      expect(solutions.sort()).toEqual(expected.sort());
    });
  });

  // Test case 3: Edge cases (empty dictionary, empty grid, no valid words)
  describe('Input edge cases', () => {
    test('Dictionary is empty', () => {
      const grid = [['a', 'b', 'c', 'd'],
                    ['e', 'f', 'g', 'h'],
                    ['i', 'j', 'k', 'l'],
                    ['m', 'n', 'o', 'p']];
      const dictionary = [];
      const expected = [];

      let solutions = findAllSolutions(grid, dictionary);

      lowercaseStringArray(solutions);
      lowercaseStringArray(expected);
      expect(solutions.sort()).toEqual(expected.sort());
    });

    test('Grid is empty', () => {
      const grid = [[]];
      const dictionary = ['test'];
      const expected = [];

      let solutions = findAllSolutions(grid, dictionary);

      lowercaseStringArray(solutions);
      lowercaseStringArray(expected);
      expect(solutions.sort()).toEqual(expected.sort());
    });

    test('No valid words in the grid', () => {
      const grid = [['x', 'y', 'z', 'w'],
                    ['q', 'r', 's', 't'],
                    ['u', 'v', 'm', 'n'],
                    ['o', 'p', 'l', 'k']];
      const dictionary = ['apple', 'orange', 'banana'];
      const expected = [];

      let solutions = findAllSolutions(grid, dictionary);

      lowercaseStringArray(solutions);
      lowercaseStringArray(expected);
      expect(solutions.sort()).toEqual(expected.sort());
    });
  });

});
