class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        scores = defaultdict(list)
        for id, score in items:
            scores[id].append(score) 

        for id, score in scores.items():
            score.sort(reverse=True)
            average = sum(score[:5]) // 5
            res.append([id, average])
        res.sort(key=lambda student: student[0])
        return res
