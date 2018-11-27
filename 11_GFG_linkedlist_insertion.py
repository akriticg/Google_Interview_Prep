'''
Given a linked list which is sorted, how will you insert in sorted way
Given a sorted linked list and a value to insert, write a function
to insert the value in sorted way.

Initial Linked List
SortedLinked List

Linked List after insertion of 9
UpdatedSortedLinked List

https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
'''


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList():

    def __init__(self):
        self.head = None

    def sortedInsert(self, newnode):
        if self.head is None:
            newnode.next = self.head
            self.head = newnode

        elif self.head.data >= newnode.getData():
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head
            while(current.next is not None and
                  current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# Driver program
llist = LinkedList()
new_node = Node(5)
llist.sortedInsert(new_node)
new_node = Node(10)
llist.sortedInsert(new_node)
new_node = Node(7)
llist.sortedInsert(new_node)
new_node = Node(3)
llist.sortedInsert(new_node)
new_node = Node(1)
llist.sortedInsert(new_node)
new_node = Node(9)
llist.sortedInsert(new_node)
print("Create Linked List")
llist.printList()
