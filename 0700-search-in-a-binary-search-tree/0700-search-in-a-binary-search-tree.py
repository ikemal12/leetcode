# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            if node.val == val:
                return node
            elif val < node.val and node.left:
                stack.append(node.left)
            elif val > node.val and node.right:
                stack.append(node.right)
        return None"""

        """
        q = deque([root])
        while q:
            node = q.popleft()
            if not node: continue
            if node.val == val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None"""