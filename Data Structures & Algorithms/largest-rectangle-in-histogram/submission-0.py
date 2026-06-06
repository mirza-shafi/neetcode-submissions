class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height) — increasing by height
        
        for i, h in enumerate(heights):
            start = i
            
            # Pop taller bars — current bar can't extend through them
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx  # current bar CAN extend back to here
            
            stack.append((start, h))
        
        # Process remaining bars — they extend all the way to the end
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        
        return max_area