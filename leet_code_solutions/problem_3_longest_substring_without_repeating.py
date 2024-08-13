# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        result = 0
        left = 0
        known_chars = set()  # we can check for something inside by O(1)
        for right, right_char in enumerate(s):
            while right_char in known_chars:
                known_chars.remove(s[left])
                left += 1
            known_chars.add(right_char)
            result = max(result, right - left + 1)
        return result


print(Solution.length_of_longest_substring("pwwkew"))
