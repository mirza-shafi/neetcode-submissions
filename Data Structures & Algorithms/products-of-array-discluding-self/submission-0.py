from typing import List
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.append(math.prod(nums[:i] + nums[i+1:]))
        return lst