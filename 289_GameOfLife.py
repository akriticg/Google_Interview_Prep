'''
289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

https://leetcode.com/problems/game-of-life/description/
'''

def gameOfLife(board):

    def LiveNeighbours(m, n, rows, columns):
        counter = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if (not (i==r and j==c)) and 0<=i<row and 0<=j<col and board[i][j]%2 == 1:
                    counter += 1
    
        return counter

    rows = len(board)
    columns = len(board[0])

    for r in range(rows):
        for c in range(columns):
            live_neighbours = LiveNeighbours(r, c, rows, columns)
            if board[r][c] == 0:
                if live_neighbours == 3:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

            else:
                if live_neighbours == 2 or live_neighbours == 3:
                    board[i][j] = 1
                
                else:
                    board[i][j] = 0


gameOfLife()