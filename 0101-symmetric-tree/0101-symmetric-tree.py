# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q: return True
            if (p and not q) or (q and not p): return False
            return (p.val == q.val) and dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(root.left, root.right)



    """        
        q = [root, root]
        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True"""
        