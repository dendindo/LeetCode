# Problem 94

class Solution:
    def inorderTraversal(self, root):

        order = []

        def traverse(node):

            if node is None:
                return

            traverse(node.left)

            order.append(node.val)

            traverse(node.right)

        traverse(root)

        return order