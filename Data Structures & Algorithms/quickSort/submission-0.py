# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs



    def helper (self, pairs, s, e):
        if (e - s + 1) <= 1:
            return

        leftPointer = s
        pivot = pairs[e]

        for i in range (s , e):
            if pairs[i].key < pivot.key:
                temp = pairs[i]
                pairs[i] = pairs[leftPointer]
                pairs[leftPointer] = temp
                leftPointer += 1
         
        pairs[e] = pairs[leftPointer]
        pairs[leftPointer] = pivot

        self.helper(pairs, s , leftPointer - 1)
        self.helper(pairs, leftPointer + 1, e) 
       