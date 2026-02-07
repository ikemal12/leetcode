# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, float("-inf"))])
        good_nodes = 0
        while q:
            node, curMax = q.popleft()
            if node.val >= curMax:
                good_nodes += 1
            if node.left:
                q.append((node.left, max(node.val, curMax)))
            if node.right:
                q.append((node.right, max(node.val, curMax)))
        return good_nodes











        """
        stack = [(root, float("-inf"))]
        good_nodes = 0
        while stack:
            node, curMax = stack.pop()
            if node.val >= curMax:
                good_nodes += 1
            if node.left:
                stack.append((node.left, max(node.val, curMax)))
            if node.right:
                stack.append((node.right, max(node.val, curMax)))
        return good_nodes"""

        """
        def dfs(node, curMax):
            if not node: return 0

            if node.val >= curMax:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, curMax) + dfs(node.right, curMax)
        
        return dfs(root, float("-inf"))"""