class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = []
        count = 0
        L = 0

        for R in range(len(arr)):
            window.append(arr[R])
            if len(window) == k:
                avg = sum(window) / len(window)
                if avg >= threshold:
                    count += 1
                window.pop(0)
        
        return count

