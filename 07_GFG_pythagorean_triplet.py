'''
Pythagorean Triplet in an array
Given an array of integers, write a function that returns true
if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Example:

Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.

https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
'''


def pyth_trip(arr):
    arr = [k*k for k in arr]
    arr.sort()

    for i in range(len(arr)-1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            # print(arr[i], arr[j], arr[k])
            if (arr[j] + arr[k] == arr[i]):
                return(arr[i], arr[j], arr[k])
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            else:
                k -= 1

print(pyth_trip([3, 1, 4, 6, 5]))
