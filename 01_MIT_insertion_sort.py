def insertion_sort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            # reverse < to > in temp < arr[j] for reverse sorting
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

    print(arr)

insertion_sort([12, 11, 13, 5, 6])
