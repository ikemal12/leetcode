# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque([root])
        res = []
        while q:
            sum = 0
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if not node: return 
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            average = sum / n
            res.append(average)
        return res
