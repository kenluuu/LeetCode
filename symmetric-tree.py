# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        l, r = [], []
        def make_l(n):
            l.append(n.val)
            if n.left is not None: make_l(n.left)
            else: l.append(None)
            if n.right is not None: make_l(n.right)
            else: l.append(None)
        def make_r(n):
            r.append(n.val)
            if n.right is not None: make_r(n.right)
            else: r.append(None)
            if n.left is not None: make_r(n.left)
            else: r.append(None)
        
        if root is None:
            return True
        
        if root.left is not None: make_l(root.left)
        if root.right is not None: make_r(root.right)
        if len(l) != len(r): return False
        
        for i in range(0, len(l)):
            if r[i] != l[i]: return False
            
        return True