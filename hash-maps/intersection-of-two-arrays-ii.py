"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""

from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        res = []
        for num in counter1:
            if num in counter2:
                x = counter1[num] if counter1[num] <= counter2[num] else counter2[num]
                res.extend(x * [num])
        return res


print(Solution().intersection([1,2], [1, 1]))