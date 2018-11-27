'''
Count triplets with sum smaller than a given value
Given an array of distinct integers and a sum value. Find count of
triplets with sum smaller than given sum value. Expected Time Complexity
is O(n2).

Examples:

Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
Output : 2
Explanation :  Below are triplets with sum less than 2
               (-2, 0, 1) and (-2, 0, 3)

Input : arr[] = {5, 1, 3, 4, 7}
        sum = 12.
Output : 4
Explanation :  Below are triplets with sum less than 4
               (1, 3, 4), (1, 3, 5), (1, 3, 7) and
               (1, 4, 5)

'''


def count_triplets(arr, x):
    arr.sort()
    print(arr)
    count = 0

    for i in range(len(arr)-1):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            if (arr[i]+arr[j]+arr[k] >= x):
                k = k-1
            else:
                count += (k-j)
                j += 1

    return count

print(count_triplets([5, 1, 3, 4, 7], 12))
