class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        del nums[j:] #actually deletes the stuff after j
        return j