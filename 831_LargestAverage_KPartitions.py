'''
813. Largest Sum of Averages

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.

https://leetcode.com/problems/largest-sum-of-averages/description/
'''


def largestSumOfAverages(A, K):

    '''
    x + y + z = k

    '''
    avg_dict = set()

    length = len(A)
    for x in range(1, length - 2):
        for y in range(x, length - 1):
            for z in range(y, length):
                if len(A[0:x]) + len(A[x:y]) + len([y:length]) == length:
                    avg = sum(A[0:x])/x + sum(A[x: y])/y + sum(A[y:])/z
                    avg_dict.add(avg)
                    print("x = ", x, "y = ", y, "z = ", z)
                    print(avg_dict)

    print(max(avg_dict))

largestSumOfAverages([9,1,2,3,9], 3)