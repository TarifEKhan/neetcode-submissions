# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            res = []
            level_length = len(queue)
            for i in range (level_length):
                curr = queue.popleft()
                res.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(res)
        return result