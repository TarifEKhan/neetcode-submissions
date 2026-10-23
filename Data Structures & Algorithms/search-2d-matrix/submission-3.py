class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[len(row) - 1]:
                continue
            elif target >= row[0] and target <= row[len(row) - 1]:
                l, r = 0, len(row) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if target > row[mid]:
                        l = mid + 1
                    elif target < row[mid]:
                        r = mid - 1
                    else:
                        return True
                return False
        return False
                    

