/**
 * Given a Boggle board and a dictionary, returns a list of available words in
 * the dictionary present inside of the Boggle board.
 * @param {string[][]} grid - The Boggle game board.
 * @param {string[]} dictionary - The list of available words.
 * @returns {string[]} solutions - Possible solutions to the Boggle board.
 */

class TrieNode {
    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        let i = 0;
        while (i < word.length) {
            if (i + 1 < word.length && ["st", "qu"].includes(word.slice(i, i + 2).toLowerCase())) {
                let seq = word.slice(i, i + 2).toLowerCase(); // Handle multi-character sequences
                if (!(seq in node.children)) {
                    node.children[seq] = new TrieNode();
                }
                node = node.children[seq];
                i += 2; // Move past the multi-character sequence
            } else {
                let char = word[i].toLowerCase();
                if (!(char in node.children)) {
                    node.children[char] = new TrieNode();
                }
                node = node.children[char];
                i++;
            }
        }
        node.isEndOfWord = true;
    }
}

class Boggle {
    constructor(grid, dictionary) {
        this.grid = grid.map(row => row.map(cell => cell.toLowerCase())); // Convert grid to lowercase
        this.trie = new Trie();
        for (let word of dictionary) {
            this.trie.insert(word.toLowerCase()); // Insert words in lowercase
        }

        this.result = new Set();
        this.rows = grid.length;
        this.cols = grid[0].length;
        this.visited = Array.from({ length: this.rows }, () => Array(this.cols).fill(false));
    }

    searchWords() {
        for (let row = 0; row < this.rows; row++) {
            for (let col = 0; col < this.cols; col++) {
                this._dfs(row, col, this.trie.root, "");
            }
        }
        return Array.from(this.result);
    }

    _dfs(row, col, node, path) {
        if (row < 0 || row >= this.rows || col < 0 || col >= this.cols || this.visited[row][col]) {
            return;
        }

        let letter = this.grid[row][col];

        // Check for multi-character sequences (like "qu" or "st")
        if (!(letter in node.children)) {
            return;
        }

        this.visited[row][col] = true;
        node = node.children[letter];
        path += letter;

        if (node.isEndOfWord) {
            this.result.add(path);
        }

        const directions = [
            [-1, 0], [1, 0], [0, -1], [0, 1],
            [-1, -1], [-1, 1], [1, -1], [1, 1]
        ];

        for (let [dx, dy] of directions) {
            this._dfs(row + dx, col + dy, node, path);
        }

        this.visited[row][col] = false;
    }
}

exports.findAllSolutions = function(grid, dictionary) {
    if (!grid || grid.length === 0 || !dictionary || dictionary.length === 0) {
        return [];
    }

    const boggle = new Boggle(grid, dictionary);
    return boggle.searchWords();
}

