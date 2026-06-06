class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # stores indices (monotonically decreasing by temperature)
        
        for i, temp in enumerate(temperatures):
            # Pop indices whose temperature is less than current
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        
        return result