'''
https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
Given an array A[] and a number x, check for pair in A[] with sum as x
Write a program that, given an array A[] of n numbers and another
 number x, determines whether or not there exist two elements in S
 whose sum is exactly x.
'''


def search(arr, x):
    set1 = set()
    for k in arr:
        temp = x - k
        if temp > 0 and temp in set1:
            print(k, temp)
        else:
            set1.add(k)

search([1, 4, 45, 6, 10, -8], 10)


def merge_sort(arr):

    if len(arr) > 1:
        L = arr[0: len(arr)//2]
        R = arr[len(arr)//2:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return(arr)


def search2(arr, x):
    arr = merge_sort(arr)
    l = 0
    r = len(arr) - 1
    print(l, r)

    while l < r:
        if (arr[l] + arr[r] == x):
            return (arr[l], arr[r])

        elif arr[l] + arr[r] < x:
            l += 1
        else:
            r -= 1

print(search2([1, 4, 45, 6, 10, -8], 10))
print(merge_sort([3, 8, 6, 5, 4, 2]))
