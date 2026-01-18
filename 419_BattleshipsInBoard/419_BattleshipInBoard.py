# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

# Example 1:


# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
# Example 2:

# Input: board = [["."]]
# Output: 0
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is either '.' or 'X'.
 

# Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0
        dirs = [(0, 1), (1, 0)]
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    res += 1
                    board[r][c] = '.'
                    # try to extend vertically or horizontally to identify the entire battleship
                    for d in dirs:
                        nr, nc = r + d[0], c + d[1]
                        while nr < m and nc < n and board[nr][nc] == 'X':
                            board[nr][nc] = '.'
                            # keep moving the same direction
                            nr, nc = r + d[0], c + d[1]
        return res
