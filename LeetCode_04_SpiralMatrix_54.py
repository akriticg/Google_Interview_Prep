'''
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all
elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

https://leetcode.com/problems/spiral-matrix/description/
'''


class Solution(object):
    def spiralOrder(self, matrix):

        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])
        r = c = di = 0

        seen = [[False] * C for _ in matrix]

        ans = []

        # clockwise
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        for _ in range(R*C):
            ans.append(matrix[r][c])
            seen[r][c] = True

            cr = r + dr[di]
            cc = c + dc[di]

            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r = cr
                c = cc

            else:
                di = (di + 1) % 4
                r = r + dr[di]
                c = c + dc[di]

        return ans


c = Solution()
print(c.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(c.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
