# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(n, i):
            if n.left is None:
                l = i
            else:
                l = traverse(n.left, i+1)
            if n.right is None:
                r = i
            else:
                r = traverse(n.right, i+1)
            return max(l, r)
        if root is None:
            return 0
        return traverse(root, 1)
