# Problem 100

def traverse(p, q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:

        return False

    return traverse(p.left, q.left) and traverse(p.right, q.right)

return traverse(p, q)