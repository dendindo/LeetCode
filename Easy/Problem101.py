# Problem 101

def isMirror(left, right):

    if left is None and right is None:
        return True
    
    if left is None or right is None:
        return False
    
    if left.val != right.val:
        return False

    return isMirror(left.left, right.right) and isMirror(left.right, right.left)           


if root is None:
    return True
else:
    return isMirror(root.left, root.right)