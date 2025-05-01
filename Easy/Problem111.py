def traverse(node):

    if node is None:
        return 0

    if node.left is None:
        return 1 + traverse(node.right)
    
    if node.right is None:
        return 1 + traverse(node.left)

    left_depth = traverse(node.left)
    right_depth = traverse(node.right)

    return 1 + min(left_depth, right_depth)

    
return traverse(root)
