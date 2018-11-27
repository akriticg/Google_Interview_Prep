'''
Convert array into Zig-Zag fashion
Given an array of distinct elements, rearrange the elements of array
in zig-zag fashion in O(n) time. The converted array should be
in form a < b > c < d > e < f.

Example:
Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

Input:  arr[] =  {1, 4, 3, 2}
Output: arr[] =  {1, 4, 2, 3}

https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/
'''


def zigzag(arr):
    flag = True
    '''
    flag = True when a < b
    '''
    for i in range(len(arr)-1):
        if flag:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if not flag:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = bool(1-flag)

    return arr

print(zigzag([4, 3, 7, 8, 6, 2, 1]))
print(zigzag([1, 4, 2, 3]))
