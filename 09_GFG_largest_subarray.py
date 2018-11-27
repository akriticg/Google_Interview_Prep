'''
Length of the largest subarray with contiguous elements | Set 1
Given an array of distinct integers, find length of the longest
subarray which contains numbers that can be arranged in a
continuous sequence.

Examples:

Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

Input:  arr[] = {14, 12, 11, 20};
Output: Length of the longest contiguous subarray is 2

Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
Output: Length of the longest contiguous subarray is 5
https://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/
'''


def largest(arr):

    maxlen = 1
    for i in range(len(arr)-1):

        minm = arr[i]
        maxm = arr[i]

        for j in range(i+1, len(arr)):

            minm = min(minm, arr[j])
            maxm = max(maxm, arr[j])

            if maxm - minm == j - i:
                maxlen = max(maxlen, maxm-minm+1)

    return maxlen

print(largest([1, 56, 58, 57, 90, 92, 94, 93, 91, 45]))
