"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left

            mid = int((left + right) / 2)
            print(left, right, "mid:", nums[mid])
            if nums[mid] == target:
                return mid

            # when the left half is sorted and contains target
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # when the right half is sorted and contains target
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    # array = [4, 5, 6, 7, 0, 1, 2]
    # trgt = 6
    array = [4,5,6,7,0,1,2]
    trgt = 0
    print(Solution().search(array, trgt))

