class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_and_position = sorted(list(zip(position, speed)), reverse = True)
        stack = []
        for i in range(len(speed_and_position)):
            time = (target - speed_and_position[i][0]) / speed_and_position[i][1]
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        print(stack)
        return len(stack)


