'''
Smallest subarray with sum greater than a given value
Given an array of integers and a number x, find the smallest
subarray with sum greater than the given value.

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.
https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
'''


def smallest(arr, x):
    sum = 0
    start = 0
    end = 0
    minlen = len(arr) + 1
    while end < len(arr):
        while sum <= x and end < len(arr):
            sum += arr[end]
            end += 1

        while sum > x and start < len(arr):
            if(end - start < minlen):
                minlen = end - start

            sum -= arr[start]
            start += 1

    return minlen

print(smallest([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
