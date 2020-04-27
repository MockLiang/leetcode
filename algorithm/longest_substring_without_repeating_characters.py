"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        memo = dict()
        begin, end = 0, 0
        n = len(s)
        while end < n:
            last = memo.get(s[end])
            memo[s[end]] = end
            if last is not None:
                maxlen = max(maxlen, end-begin)
                begin = max(begin, last + 1)
            end += 1
        maxlen = max(maxlen, end-begin)
        return maxlen


print(Solution().lengthOfLongestSubstring("abcabcbb"))
