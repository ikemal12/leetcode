class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        return (s+s).find(goal) != -1


        """
        q = collections.deque(s)
        g = collections.deque(goal)

        for i in range(len(q)):
            c = q.popleft()
            q.append(c)
            if q == g: return True
        return False"""