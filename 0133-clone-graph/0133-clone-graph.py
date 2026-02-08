"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        done = set()
        stack = [node]

        while stack:
            node = stack.pop()
            done.add(node.val)

            if node.val not in done:
                new = Node(node.val)

                newNs = []
                for n in node.neighbours:
                    newN = Node(n.val)
                    newNs.append(newN)
                    stack.append(n)
        









        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None







        oldToClone = {}

        def dfs(node):
            if node in oldToClone:
                return oldToClone[node]
            
            copy = Node(node.val)
            oldToClone[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None