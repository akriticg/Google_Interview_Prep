'''
487. Max Consecutive Ones II
Given a binary array, find the maximum number of consecutive 1s
in this array if you can flip at most one 0.

Example 1:

Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum
number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In
other words, you can't store all numbers coming from the stream as it's
too large to hold in memory. Could you solve it efficiently?
https://leetcode.com/problems/max-consecutive-ones-ii/description/
'''


def findMaxConsecutiveOnes(nums):

    zero = 1
    current_num = 0
    max_num = 0
    prev_num = -1

    for k in nums:
        if k == 0:
            prev_num = current_num
            current_num = 0

        else:
            current_num += k

        max_num = max(max_num, prev_num + zero + current_num)

        print("k = ", k)
        print("prev_num", prev_num)
        print("curr_num", current_num)
        print("max num =", max_num)

    return max_num

print(findMaxConsecutiveOnes([1, 0, 1, 0, 1, 0, 1, 1, 0]))