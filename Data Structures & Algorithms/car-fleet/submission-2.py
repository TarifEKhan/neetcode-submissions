class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_and_speed = sorted(list(zip(position, speed)), reverse = True)
        stack = []
        for car in position_and_speed:
            time = (target - car[0]) / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)
            
            
            
        print(stack)
        return len(stack)
