class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def printLevelOrder(root):
    if root.value is None:
        return
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        node = queue.pop(0)
        print(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)
