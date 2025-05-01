# Problem 110

def traverse(node):

    if node is None:
        return 0

    left_result = traverse(node.left)
    right_result = traverse(node.right)

    if left_result == -1 or right_result == -1:
        return -1
    
    if abs(left_result - right_result) > 1:
        return -1

    height = 1 + max(left_result, right_result)

    return height

result = traverse(root)

if result == -1:
    return False
else:
    return True