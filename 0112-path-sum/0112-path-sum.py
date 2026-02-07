# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum - root.val)]
        while stack:
            node, sum = stack.pop()
            if not node.left and not node.right and sum == 0:
                return True
            if node.left:
                stack.append((node.left, sum - node.left.val))
            if node.right:
                stack.append((node.right, sum - node.right.val))
        return False
        """
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        return dfs(root, 0)"""









        def dfs(node, curSum):
            if not node: return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfs(node.left, curSum) or
                    dfs(node.right, curSum))
        return dfs(root, 0)