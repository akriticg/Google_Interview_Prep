'''
Generate all possible sorted arrays from alternate elements of two
 given sorted arrays
Given two sorted arrays A and B, generate all possible arrays such that
 first element is taken from A then from B then from A and
 so on in increasing order till the arrays exhausted. The generated
 arrays should end with an element from B.

For Example
A = {10, 15, 25}
B = {1, 5, 20, 30}

The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30

https://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/

  '''


def sorted(x, y):
    i = j = k = 0
    a = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            a[k] = x[i]
            x += 1
        else:
            a[k] = y[j]
            j += 1
        k += 1
        print(a)

sorted([10, 15, 25], [1, 5, 20, 30])
