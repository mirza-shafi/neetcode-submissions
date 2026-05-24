from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > 1:
                return True
        return False

nums = [1, 2, 3, 3]
sol = Solution()
x = sol.hasDuplicate(nums)
print(x) 
