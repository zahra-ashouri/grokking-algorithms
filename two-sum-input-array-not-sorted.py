"""
https://leetcode.com/problems/two-sum/description/

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = dict()

        for i, num in enumerate(nums):
            x = target - num
            if x in index_map:
                return [index_map[x], i]
            index_map[num] = i
        return [-1, -1]


print(Solution().twoSum(nums=[3, 3], target=6))
