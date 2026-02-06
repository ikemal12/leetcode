# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return False
        if root == p or root == q: 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right
            
        """
        self.res = None
        self.dfs(root, p, q)
        return self.res

    def dfs(self, root, p, q):
        if not root: return False
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        mid = root == p or root == q
        if left + right + mid >= 2:
            self.res = root
        return left or right or mid"""
        







        if not root: return None
        if root == p or root == q: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r









        if not root:
            return None

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r

        