"""
https://leetcode.com/problems/3sum/

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(numbers: List[int], start: int, target: int):
            left = start
            right = len(numbers) - 1
            answers = []
            while left < right:
                summ = numbers[left] + numbers[right]
                if summ == target:
                    answers.append([numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                elif summ < target:
                    left += 1
                else:
                    right -= 1
            return answers

        # print(twoSum([-2,0,1,1,2], 1, 2))
        nums = sorted(nums)
        res = []
        for i, num in enumerate(nums):
            if i == len(nums) - 2:
                break
            output = twoSum(nums, start=i + 1, target=-1 * num)
            if output:
                for li in output:
                    if (li + [num]) not in res:
                        res.append(li + [num])

        return res


print(Solution().threeSum([-2,0,0,2,2]))
