'''
73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

https://leetcode.com/problems/set-matrix-zeroes/description/
'''


def setZeroes(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    zero_rows = set()
    zero_columns = set()

    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                zero_columns.add(c)
                zero_rows.add(r)

    for r in range(rows):
        for c in range(columns):
            if r in zero_rows or c in zero_columns:
                matrix[r][c] = 0

    return matrix

print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
