def get_ancestor(D, A, i):
    if D == 0:
        return i

    new_index = A[i]
    if new_index < 0:
        return -1
    return get_ancestor(D-1, A, new_index)


def solution(D, A):
    dist = [-1]

    for i in range(1, len(A)):
        a = get_ancestor(D, A, i)
        dist.append(a)

    return dist