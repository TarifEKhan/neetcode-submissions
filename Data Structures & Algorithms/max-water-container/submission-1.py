class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = float("-inf")
        l = 0
        r = len(heights) - 1
        res = float("-inf")
        while l < r:
            current_max = (r - l) * min(heights[l], heights[r])
            if current_max > res:
                res = current_max

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res