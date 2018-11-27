
def solution(stores, houses):

    distance = {}
    output = [1000000] * len(houses)

    for k in range(len(houses)):
        individual_dist = []
        for j in range(len(stores)):
            individual_dist.append(abs(houses[k] - stores[j]))

        distance[houses[k]] = individual_dist

    for l in range(len(output)):
        k = distance[houses[l]]
        for j in range(len(k)):

            if k[j] == output[l]:
                if stores[j] < stores[key]:
                    output[l] = k[j]
                    key = j

            if k[j] < output[l]:
                output[l] = k[j]
                key = j

        output[l] = stores[key]

    return output

stores = [18, 5, 20, 11, 16]
houses = [5, 10, 17]
print(solution(stores, houses))




'''
Use a BST
Make a BST of the stores and then traverse the BST till you reach the leaf node while updating the closest store. Do this for every house and return to the array.

class BST:
    class Node:
        val = None
        left = None
        right = None

        def __init__(self, val):
            self.val = val

    root = None

    def __init__(self, array):
        for i in array:
            self.insert(i)

    def insert_bst(self, tree_node, new_node):
        if new_node.val < tree_node.val:
            if tree_node.left:
                self.insert_bst(tree_node.left, new_node)
            else:
                tree_node.left = new_node

    def insert(self, val):
        new_node = self.Node(val)
        if not self.root:
            self.root = new_node
            return
        self.insert_bst(self.root, new_node)
        return

def bst_search_curr(tree_node, house, curr_closest):
    if not tree_node:
        return curr_closest
    if abs(tree_node.val - house) > abs(curr_closes - house):
        return curr_closest

    else:
        curr_closest = tree_node.val
        if house < tree_node.val:
            return bst_search_curr(tree_node.left, house, curr_closest)
        else:
            return bst_search_curr(root_node.right, house, curr_closest)


def bst_search(tree_node, house):
    curr_closes = root_node.val
    if house < tree_node.val:
            return bst_search_curr(tree_node.left, house, curr_closest)
        else:
            return bst_search_curr(root_node.right, house, curr_closest)




def solution(stores, houses):
    stores_bst = BST(stores)
    closest = []
    for h in houses:
        closest.append(bst_search(stores_bst.root, h))
    return closest

'''