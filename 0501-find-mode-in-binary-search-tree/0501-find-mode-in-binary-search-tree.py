# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev, curCount, maxCount, modes = None, 0, 0, []
        def inorder(node):
            nonlocal prev, curCount, maxCount, modes
            if not node: return
            if node.left:
                inorder(node.left)
            if node.val == prev:
                curCount += 1
            else:
                curCount = 1
                prev = node.val
            if curCount > maxCount:
                maxCount = curCount
                modes = [node.val]
            elif curCount == maxCount:
                modes.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return modes

        """counts = {}
        for n in res:
            counts[n] = 1 + counts.get(n, 0)
        maxCount = max(counts.values())
        return [num for num, count in counts.items() if count == maxCount]"""


        