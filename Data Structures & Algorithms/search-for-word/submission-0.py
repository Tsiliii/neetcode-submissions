class Solution:            
    def try_tile(self, board, i, j, word, index):
        self.used.add((i,j))
        if self.recurse(board, i, j, word, index+1): 
            return True
        self.used.remove((i, j))
        return False


    def recurse(self, board, i, j, word, index):
        if index == len(word):
            return True
        if i > 0 and board[i-1][j] == word[index] and (i-1,j) not in self.used:
            if self.try_tile(board, i-1, j, word, index):
                return True
        if i < len(board)-1 and board[i+1][j] == word[index] and (i+1,j) not in self.used:
            if self.try_tile(board, i+1, j, word, index):
                return True
        if j > 0 and board[i][j-1] == word[index] and (i,j-1) not in self.used:
            if self.try_tile(board, i, j-1, word, index):
                return True
        if j < len(board[0])-1 and board[i][j+1] == word[index] and (i,j+1) not in self.used:
            if self.try_tile(board, i, j+1, word, index):
                return True

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.used = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:        
                    self.used.add((i,j))
                    if self.recurse(board, i, j, word, 1):
                        return True
                    self.used.remove((i,j))
        return False

        