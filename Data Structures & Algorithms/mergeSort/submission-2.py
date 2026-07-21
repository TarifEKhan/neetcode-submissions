# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        left_arr = pairs[:len(pairs)//2]
        right_arr = pairs[len(pairs)//2:]

        left_arr = self.mergeSort(left_arr)
        right_arr = self.mergeSort(right_arr)

        i = 0
        j = 0
        res = []

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].key <= right_arr[j].key:
                res.append(left_arr[i])
                i += 1
            else:
                res.append(right_arr[j])
                j += 1
            
        while i < len(left_arr):
            res.append(left_arr[i])
            i += 1

        while j < len(right_arr):
            res.append(right_arr[j])
            j += 1

        return res
