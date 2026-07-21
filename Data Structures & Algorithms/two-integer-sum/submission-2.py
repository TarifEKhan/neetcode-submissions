class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            eureka_num = target - nums[i]
            if eureka_num in map:
                return [map[eureka_num], i]

            else:
                map[nums[i]] = i