class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

        """
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        res = [num for num, count in counts[:k]]
        return res"""














        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




















        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        res = []
        for i in range(k):
            res.append(list(counts.keys())[i])
        return res
