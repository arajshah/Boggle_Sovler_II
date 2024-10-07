"""
Starter Asssignment Software Engineering 
Araj Shah
@03056118 
"""

class TrieNode:
    def __init__(self):
        # Each TrieNode contains a dictionary of children (letters) and a boolean flag indicating if it's the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()
    
    def insert(self, word):
        # Insert a word into the Trie
        node = self.root
        i = 0
        while i < len(word):
            # Check for multi-character sequences like "St" or "Qu"
            if i + 1 < len(word) and word[i:i+2] in ["St", "Qu"]:  # Adjust this based on known sequences
                seq = word[i:i+2]
                if seq not in node.children:
                    node.children[seq] = TrieNode()
                node = node.children[seq]
                i += 2  # Move past the multi-character sequence
            else:
                char = word[i]
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                i += 1
        node.is_end_of_word = True

class Boggle:
    def __init__(self, grid, dictionary):
        # Initialize the Boggle game with the grid and dictionary
        self.grid = grid
        
        # Create a Trie and insert all words from the dictionary into the Trie
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word)
        
        # Result set to store found words
        self.result = set()
        
        # Number of rows and columns in the grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        # Visited array to track visited cells during DFS
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
    
    def search_words(self):
        # Iterate over each cell in the grid and start a DFS search
        for row in range(self.rows):
            for col in range(self.cols):
                # Start DFS from each cell
                self._dfs(row, col, self.trie.root, "")
        
        # Return the list of found words
        return list(self.result)
    
    def _dfs(self, row, col, node, path):
        # Boundary checks to ensure we're within the grid
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.visited[row][col]:
            return
        
        # Get the current letter from the grid
        letter = self.grid[row][col]
        
        # If the letter is not a valid child in the Trie, prune the search
        if letter not in node.children:
            return
        
        # Mark the cell as visited
        self.visited[row][col] = True
        
        # Move to the next node in the Trie corresponding to the letter
        node = node.children[letter]
        
        # Append the letter to the current path
        path += letter
        
        # If we reach the end of a word in the Trie, add it to the result set
        if node.is_end_of_word:
            self.result.add(path)
        
        # Explore all 8 possible directions around the current cell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            self._dfs(row + dx, col + dy, node, path)
        
        # Unmark the cell as visited when backtracking
        self.visited[row][col] = False

def main():
    grid = [ ["T", "R", "E", "E"],
            ["A", "St", "O", "Qu"],
            ["S", "M", "T", "N"],
            ["P", "L", "A", "Y"]
           ]
    
    dictionary = ["TREE", "TO", "StONE", "StOQuE", "QuEEN", "PLAY", "StO", "StREAM"]

    mygame = Boggle(grid, dictionary)
    foundWords = mygame.search_words()
    print("Found Words: ", foundWords)
    
if __name__ == "__main__":
    main()