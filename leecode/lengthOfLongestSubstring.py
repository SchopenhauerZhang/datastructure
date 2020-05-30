# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
#
def lengthOfLongestSubstring( s: str)->int:
    ss = dict()

    for i in s:
        ss[i] = 1

    window = dict()
    left = right = 0
    max_len = 0
    mx = 0
    

    while right < len(s):
        char = s[right]
        right += 1
        if char not in window:
            window[char] = 0
            window[char] += 1
        else:
            window[char] += 1

        if window[char] == ss[char]:
            max_len += 1
        
        while max_len < (right - left):

            char = s[left]
            if max_len > mx:
                mx = max_len

            if char in window:
                if window[char] == ss[char]:
                    max_len -= 1
                window[char] -= 1
            
            left += 1

    return max_len  if max_len > mx else mx

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)
        length = 0
        for i in range(0, len(s)):
            length = max(length, find_left(s, i))
        return length




