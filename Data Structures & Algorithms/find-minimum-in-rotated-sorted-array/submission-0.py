class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, mid could be the minimum, or the minimum is to the left.
            else:
                right = mid
                
        # When left == right, it will point directly to the minimum element.
        return nums[left]