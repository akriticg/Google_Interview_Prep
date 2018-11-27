'''
Given two linked lists, represented as linked lists (every character
is a node in linked list). Write a function compare() that works
similar to strcmp(), i.e., it returns 0 if both strings are same,
1 if first linked list is lexicographically greater, and -1 if
second string is lexicographically greater.

Examples:

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s->b
Output: -1

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s
Output: 1

Input: list1 = g->e->e->k->s
       list2 = g->e->e->k->s
Output: 0

https://www.geeksforgeeks.org/compare-two-strings-represented-as-linked-lists/
'''


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def compare(l1, l2):
    while (l1 and l2 and l1.data == l2.data):
        l1 = l1.next
        l2 = l2.next

    if(l1 and l2):
        return 1 if l1.data > l2.data else -1
    if(l1 and not l2):
        return 1
    if(l2 and not l1):
        return -1
    return 0

list1 = Node('g')
list1.next = Node('e')
list1.next.next = Node('e')
list1.next.next.next = Node('k')
list1.next.next.next.next = Node('s')
list1.next.next.next.next.next = Node('b')

list2 = Node('g')
list2.next = Node('e')
list2.next.next = Node('e')
list2.next.next.next = Node('k')
list2.next.next.next.next = Node('s')
list2.next.next.next.next.next = Node('a')

print(compare(list1, list2))
