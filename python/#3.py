class Solution:
    def lengthOfLongestSubstring(self, s):
        tmp_set = set()
        max_num = tmp_nums = 0
        for sub_s in s:
            if sub_s in tmp_set:
                max_num = tmp_nums if tmp_nums > max_num else max_num
                tmp_set.clear()
                tmp_nums = 0
            tmp_nums += 1
            tmp_set.add(sub_s)
        else:
            max_num = tmp_nums if tmp_nums > max_num else max_num
        return max_num

print(Solution().lengthOfLongestSubstring("dvdf"))
