def merge_sort(a):

    if len(a) > 1:

        m = len(a) // 2
        L = a[:m]
        R = a[m:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1

    print(a)

merge_sort([12, 11, 13, 5, 6])
