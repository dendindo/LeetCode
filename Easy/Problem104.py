# Problem 104


def traverse(node):

    if node is None:
        return 0
    else:
        left_depth = traverse(node.left)
        right_depth = traverse(node.right)

    return 1 + max(left_depth, right_depth)

