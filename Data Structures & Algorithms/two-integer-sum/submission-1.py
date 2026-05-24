class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        for i in range(len(nums)):
            x = target - nums[i]
            if x in seen:
                return  [nums.index(x), i]
            seen.append(nums[i])
nums = [5,5]
target = 10
sol = Solution()
print(sol.twoSum(nums,target))