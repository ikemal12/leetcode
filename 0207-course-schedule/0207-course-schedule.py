class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
        
        visit, safe = set(), set()
        def dfs(course):
            if course in safe:
                return True
            if course not in graph:
                safe.add(course)
                return True
            if course in visit:
                return False
            visit.add(course)
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            visit.remove(course)
            safe.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True













"""
        # map each course to prereq list
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the current DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


"""







"""

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
"""