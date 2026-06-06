class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair and sort by position descending (closest to target first)
        pairs = sorted(zip(position, speed), reverse=True)
        
        stack = []  # stores time-to-target for each fleet
        
        for pos, spd in pairs:
            time = (target - pos) / spd
            stack.append(time)
            
            # If current car arrives <= the car ahead, they merge into one fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)