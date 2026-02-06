# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        q = deque([root])
        level = 0

        while q:
            nodes = []
            for _ in range(len(q)):
                node = q.popleft()
                nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

            if level % 2 == 0:
                l, r = 0, len(nodes) - 1
                while l < r:
                    nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
                    l += 1
                    r -= 1

        return root

"""
    [2,3,5,8,13,21,34]
    q = [3]
    level = 1
"""