class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n_set = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                n_set.remove(nums[L])
                L += 1
            
            if nums[R] in n_set:
                return True
            
            n_set.add(nums[R])
        return False