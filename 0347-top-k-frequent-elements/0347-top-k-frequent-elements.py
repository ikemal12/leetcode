class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        res = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            res[count].append(num)
        
        counter = k
        final = []
        for i in range(len(res)-1, -1, -1):
            if res[i] and counter > 0:
                if len(res[i]) == 1:
                    final.append(res[i][0])
                    counter -= 1
                else:
                    for val in res[i]:
                        if counter > 0:
                            final.append(val)
                            counter -= 1
                

                if counter <= 0:
                    break

        return final

        """
        [1,2,1,2,1,2,3,1,3,2], k=2
        counts = {1:4, 2:4, 3:2}
        res = [0,0,3,0,[1,2],0,0,0,0,0,0]
        final = [1, 2]
        """




        """
        if k == len(nums): return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)"""

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
