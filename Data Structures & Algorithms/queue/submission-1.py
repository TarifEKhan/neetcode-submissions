class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = ListNode(value)
        temp = self.tail.prev
        temp.next = node
        node.next = self.tail
        node.prev = temp
        self.tail.prev = node


    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        


    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            curr = self.tail.prev
            curr.prev.next = self.tail
            self.tail.prev = curr.prev
            return curr.val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            curr = self.head.next
            curr.next.prev = self.head
            self.head.next = curr.next
            return curr.val
