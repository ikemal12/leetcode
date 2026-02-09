class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
            return 
            
        n = len(isConnected)
        visited = set()
        province = 0
        for i in range(n):
            if i not in visited:
                province += 1
                dfs(i)
        return province



        """
        n = len(isConnected)
        adj = { i:[] for i in range(1,n+1)}
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    adj[i+1].append(j+1)
        
        visited = set()
        def bfs(i):
            q = collections.deque([i])
            while q:
                node = q.popleft()
                visited.add(node)
                for c in adj[node]:
                    if c not in visited:
                        q.append(c)

        provinces = 0
        for i in range(1,n+1):
            if i not in visited:
                bfs(i)
                provinces += 1
        return provinces"""



"""
[[1,1,0],
 [1,1,0],
 [0,0,1]]

adj = { 1:[], 2:[], 3:[]}
"""