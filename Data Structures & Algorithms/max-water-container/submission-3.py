class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            current_capacity = (r - l) * min(heights[l], heights[r])
            if current_capacity > res:
                res = current_capacity
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
