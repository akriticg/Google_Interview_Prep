class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def height(node):
    if node is None:
        return 0

    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.value)
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def printLevelOrder(root):
    for i in range(1, height(root)+1):
        printGivenLevel(root, i)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printLevelOrder(root)
