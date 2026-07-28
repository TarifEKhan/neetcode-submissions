class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        l = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, value in count.items():
            l[value].append(key)

        res = []
        for i in range(len(l) - 1, 0, -1):
            for n in l[i]:
                res.append(n)
                if len(res) == k:
                    return res