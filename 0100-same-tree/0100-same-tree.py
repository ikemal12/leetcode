# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if (p and not q) or (q and not p): 
                return False
            elif not p and not q:
                return True
            else:
                if p.val == q.val:
                    return dfs(p.left, q.left) and dfs(p.right, q.right)
                else:
                    return False
            
        return dfs(p, q)









        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                (self.isSameTree(p.right, q.right)))
