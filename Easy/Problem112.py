# Problem 112

def calculate(node, sum):

    if node is None:
        return False

    if node.left is None and node.right is None:
        return node.val == sum
    
    if calculate(node.left, sum - node.val) or calculate(node.right, sum - node.val):
        return True
    else:
        return False


return calculate(root, targetSum)