'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
https://www.geeksforgeeks.org/array-rotation/
input : [1, 2, 3, 4, 5, 6, 7]
rotation by 2 will yield :
output : [3, 4, 5, 6, 7, 1, 2]
'''

'''
My notes :
I can make a temp array from the elements I need to move and the
'''


def rotate(arr, d, n):

    temp = list()
    new = list()
    for i in range(d):
        temp.append(arr[i])
    print(temp)
    for i in range(n):
        if i in range(d):
            pass
        else:
            new.append(arr[i])
    for i in temp:
        new.append(i)
    print(new)


def rotate1(arr, d, n):

    temp = arr[:d]
    new = arr[d:]

    for k in temp:
        new.append(k)

    print(new)


def rotate2(arr, d, n):
    temp = arr[:d]
    print(temp)
    for k in range(d):

        for i in range(n-1):
            arr[i] = arr[i+1]

        arr[n-d] = temp[d]
    print(arr)


def rotate3(arr, d, n):
    for i in range(gcd(d, n)):
        k = i
        temp = arr[i]
        while True:
            j = k + d
            if j >= n:
                j = j - n
            if j == i:
                break
            arr[k] = arr[j]
            k = j
        arr[k] = temp
    print(arr)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

rotate3([1, 2, 3, 4, 5, 6, 7], 2, 7)
