# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            root, low, high = stack.pop()
            if not root: continue
            if not (low < root.val < high): return False
            stack.append((root.left, low, root.val))
            stack.append((root.right, root.val, high))
        return True


        """
        def dfs(node, low, high):
            if not node: return True
            if not (low < node.val < high): return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float("-inf"), float("inf"))"""








        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))







        
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))