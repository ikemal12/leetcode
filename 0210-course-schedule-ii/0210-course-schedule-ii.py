class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = collections.defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        res = []
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        

        














        # build adjacency list mapping courses to their prereqs
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet, cycle = set(), set()
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visitSet:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visitSet.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return output
            













        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit, cycle = set(), set()
        order = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visit.add(crs)
            order.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return order

