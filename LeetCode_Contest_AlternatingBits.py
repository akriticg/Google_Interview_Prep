'''
693. Binary Number with Alternating Bits

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:

Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:

Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:

Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:

Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = ""

        while n > 0:
            r = n % 2
            bits += str(r)
            n = n//2

        alternating = True

        for k in range(len(bits)-1):
            if bits[k] == bits[k+1]:
                alternating = False
                return alternating

        return alternating

s = Solution()
print(s.hasAlternatingBits(5))