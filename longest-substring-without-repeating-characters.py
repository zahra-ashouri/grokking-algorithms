"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""


class Solution:

    # Solved with left, right pointers
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

        return max_length

    # Solved with a map, holding the last index of the duplicate occurence
    def length_of_longest_substring(self, s: str) -> int:
        left, right = 0, 0
        index_map = dict()
        max_length = 0

        while right < len(s):
            if s[right] in index_map:
                max_length = max(max_length, right - left)
                left = max(left, index_map[s[right]]+1)
            index_map[s[right]] = right
            right += 1

        max_length = max(max_length, right - left)
        return max_length


print(Solution().lengthOfLongestSubstring("aabbccd"))
print(Solution().length_of_longest_substring("aabbccd"))