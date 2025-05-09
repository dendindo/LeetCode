# Problem 145

order = []


def traverse(node):

    if node is None:
        return

    

    traverse(node.left)

    traverse(node.right)

    order.append(node.val)

traverse(root)
