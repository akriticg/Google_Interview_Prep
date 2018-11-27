'''
41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
https://leetcode.com/problems/first-missing-positive/description/
'''


def firstMissingPositive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]
        for i in nums:
            l = len(res)-1
            print("l = ", l)
            print("res = ", res)

            if i > 0:
                if i > l:
                    res = res + (i-l-1)*[0]+[1]
                else:
                    res[i] = 1

        res.append(0)

        for i in range(1, len(res)):
            if res[i] == 0:
                return i

print(firstMissingPositive([8, 7, 6, 5]))
