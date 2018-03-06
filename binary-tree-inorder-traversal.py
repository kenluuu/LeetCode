# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None: return []

        # recursive solution
        # return self.inorderTraversalRecu(root, [])

        #iterative solution
        return self.inorderTraversalIter(root, [], [])



    

    def inorderTraversalRecu(self, root, stack):
        if root.left is not None:
            stack = self.inorderTraversalRecu(root.left, stack)
        stack.append(root.val)
        if root.right is not None:
            stack = self.inorderTraversalRecu(root.right, stack)
        return stack

    def inorderTraversalIter(self, root, node_stack, stack):
        curr = root
        done = False
        while not done:
            if curr is not None:
                node_stack.append(curr)
                curr = curr.left
            else:
                if len(node_stack) > 0:
                    curr = node_stack.pop()
                    stack.append(curr.val)
                    curr = curr.right
                else:
                    done = True

        return stack
