class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left half is normally sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Otherwise, the right half must be normally sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1