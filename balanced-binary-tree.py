# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        if root is None: return True
        is_balanced = self.isBalancedUtil(root, 0)
        if not is_balanced: return False
        return True

    def isBalancedUtil(self, node, h):
        if node is None:
            return h
        left_height = self.isBalancedUtil(node.left, h+1)
        if not left_height: return False
        right_height = self.isBalancedUtil(node.right, h+1)
        if not right_height: return False
        if abs(left_height-right_height) > 1:
            return False
        return max(left_height, right_height)
