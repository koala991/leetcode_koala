class Solution:
    def lengthOfLongestSubstring(self, s):
        max_num = lower = up = 0
        for up in range(len(s)):
            ind = s.find(s[up], lower, up)
            if ind > -1:
                max_num = max(up - lower, max_num)
                lower = ind + 1
        return min(max(up + 1 - lower, max_num), len(s))

print(Solution().lengthOfLongestSubstring("abcabcbb"))
