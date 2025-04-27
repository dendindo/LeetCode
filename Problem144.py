# Problem 144

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []


        def traverse(node):

            if node is None:
                return

            order.append(node.val)

            traverse(node.left)

            traverse(node.right)

        traverse(root)

        return order