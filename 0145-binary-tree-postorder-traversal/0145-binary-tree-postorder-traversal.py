# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, stack = [], []
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        return res[::-1]



        """
        if not root: return []
        res = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res"""