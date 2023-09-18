"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        leftm, rightm = -1, -1
        # To find the left-most
        while left < right:
            mid = (left + right) // 2
            print("left:", left, "right:", right, "nums[mid]:", nums[mid])
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        leftm = left
        print("*****")
        print("left:", left, "right:", right)

        # To find the right-most
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            print("left:", left, "right:", right, "nums[mid]:", nums[mid])
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        print("*****")
        print("left:", left, "right:", right)
        if nums[right] == target:
            rightm = right
        elif nums[left] == target:
            rightm = left

        return [leftm, rightm]


# print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([1], 1))