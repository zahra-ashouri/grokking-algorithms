"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left + 1, right + 1]
            elif summ < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


numbers = [2, 3, 4, 4, 6]
target = 7
print(Solution().twoSum(numbers, target))
