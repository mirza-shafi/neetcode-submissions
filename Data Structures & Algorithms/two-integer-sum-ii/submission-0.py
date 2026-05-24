class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            elif current_sum < target:
                # Need a larger sum, move left pointer right
                left += 1
            else:
                # Need a smaller sum, move right pointer left
                right -= 1
        
        # Should never reach here based on problem constraints
        return []
