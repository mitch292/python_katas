class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

tree_vals = {}

def check_bst(root):

    if root is None:
        return True

    tree_vals[root.data] = tree_vals.get(root.data, 0) + 1


    if root.left is not None:
        if root.left.data > root.data:
            return False

    if root.right is not None:
        if root.right.data < root.data:
            return False

    if not check_bst(root.right) or not check_bst(root.left):
        return False
    
    count_above_one = [val for val in tree_vals.values() if val > 1]

    return len(count_above_one) == 0


if __name__ == "__main__":
    root = Node(2)
    depth_one = root.left = Node(1)
    depth_one_right = root.right = Node(2)
    print(check_bst(root))