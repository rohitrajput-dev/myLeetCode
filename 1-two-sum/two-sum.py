from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        # Dictionary to store the numbers and their indices
        num_index = {}
        
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_index:
                return [num_index[comp],i]
            num_index[num] = i
        return None