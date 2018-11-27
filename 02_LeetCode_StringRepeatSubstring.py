'''
Repeated String Match

Given two strings A and B, find the minimum number of times A has
to be repeated such that B is a substring of it. If no such solution,
return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”),
B is a substring of it; and B is not a substring of A repeated
two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

https://leetcode.com/explore/interview/card/google/67/sql-2/469/
'''


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(set(A)) < len(set(B)) or len(set(A+B)) != len(set(A)):
            return -1

        i = 1
        increment = A

        while True:
            if B in increment:
                return i
            if len(increment) - len(A) > len(B) - 1:
                return -1
            increment += A
            i += 1
