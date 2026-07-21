class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.bubbleUp(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.bubbleDown(1)
        return res

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in reversed(range(1 , len(self.heap) // 2 + 1)):
            self.bubbleDown(i)

    def bubbleUp(self, index):
        parent = index // 2
        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[parent] , self.heap[index] = self.heap[index] , self.heap[parent]
            index = parent
            parent = index // 2

    def bubbleDown(self, index):
        while index * 2 < len(self.heap):
            if index * 2 + 1 < len(self.heap) and self.heap[index * 2 + 1] < self.heap[index * 2] and self.heap[index] > self.heap[index * 2 + 1]:
                self.heap[index], self.heap[index * 2 + 1] = self.heap[index * 2 + 1], self.heap[index]
                index = index * 2 + 1
            
            elif self.heap[index] > self.heap[index * 2]:
                self.heap[index] , self.heap[index * 2] = self.heap[index * 2] , self.heap[index]
                index = index * 2
            
            else:
                return