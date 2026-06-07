import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The range of possible eating speeds
        left, right = 1, max(piles)
        res = right  # Default upper bound is always valid
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Calculate total hours spent at eating speed `mid`
            total_hours = 0
            for pile in piles:
                # Math ceiling division to get hours for current pile
                total_hours += (pile + mid - 1) // mid
                
            # If Koko can finish within h hours, try to find a smaller valid speed
            if total_hours <= h:
                res = mid
                right = mid - 1
            else:
                # Too slow, increase the speed bound
                left = mid + 1
                
        return res