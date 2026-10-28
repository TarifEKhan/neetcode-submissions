class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        top, bot = 0, row - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
                
        if top > bot:
            return False

        candidate_row = (top + bot) // 2
        l, r = 0, len(matrix[candidate_row]) - 1
        while l <= r:
            middle = (l + r) // 2
            if target > matrix[candidate_row][middle]:
                l = middle + 1
            elif target < matrix[candidate_row][middle]:
                r = middle - 1
            else:
                return True
        return False