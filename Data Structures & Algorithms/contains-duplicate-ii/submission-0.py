class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        num_set = set()

        for R in range(len(nums)):
            if R - L > k:
                num_set.remove(nums[L])
                L += 1
            if nums[R] in num_set:
                return True
            num_set.add(nums[R])
        return False