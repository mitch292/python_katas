class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None



def height(root):

    if root is None:
        return -1

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1
