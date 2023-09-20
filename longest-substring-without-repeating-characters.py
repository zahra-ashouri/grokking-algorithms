"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left, right = 0, 0
        seen = set()
        max_length = 0

        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                max_length = max(len(seen), max_length)
                right += 1

        max_length = max((right - left), max_length)
        return max_length


print(Solution().lengthOfLongestSubstring("pwwkew"))
