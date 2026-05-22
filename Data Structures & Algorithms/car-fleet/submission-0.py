class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car with its time to reach target, sorted by position (closest first)
        pairs = sorted(zip(position, speed), reverse=True)
        
        stack = []  # tracks time-to-target for each fleet's lead car
        
        for pos, spd in pairs:
            time = (target - pos) / spd
            # Only push if this car is slower than the car ahead (new fleet)
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack) 