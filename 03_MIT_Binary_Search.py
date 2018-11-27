def binary_search(arr, elem):
    '''
    assume sorted array arr and need to find elem in the array
    '''
    l = 0
    r = len(arr)

    while r >= l:
        m = (r + l) // 2
        if arr[m] < elem:
            l = m + 1
        elif arr[m] > elem:
            r = m - 1
        else:
            return m

def binary_search2(arr, l)
print(binary_search([1, 2, 3, 4, 5, 6], 2))
