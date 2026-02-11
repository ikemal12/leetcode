# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(cur):
            return inorder(cur.left) + [cur.val] + inorder(cur.right) if cur else []
        return inorder(root)[k - 1]










       

        """
        stack = []
        cur = root
        n = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k: return cur.val
            cur = cur.right
        return res[k-1]"""
        """
        res = []
        def dfs(node):
            if not node: return 
            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return res[k-1]"""