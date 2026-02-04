# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([root])
        depth = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
        return depth

        [9, 15]


        """
        if not root: return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))"""









        # iterative dfs
        stack = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return res

        # bfs
        if not root: return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return level

        #recursive dfs
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))








        if not root:
            return 0

        levels = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels += 1
        return levels

        """
        def dfs(curr):
            if not curr:
                return 0
            return 1 + max(dfs(curr.left), dfs(curr.right))
        return dfs(root)"""