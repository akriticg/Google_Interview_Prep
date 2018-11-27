'''
66. Plus One
Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the
head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

https://leetcode.com/problems/plus-one/description/
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for k in range(len(digits)-1, -1, -1):

            if digits[k] + carry == 10:
                carry = 1
                digits[k] = 0
            else:
                digits[k] += carry
                carry = 0

        if carry == 1:
            return [1] + [0]*len(digits)

        return digits
