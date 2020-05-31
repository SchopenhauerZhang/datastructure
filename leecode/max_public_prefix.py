class Solution:
    def longestCommonPrefix(self, strs: list=[]) -> str:
        """
        编写一个函数来查找字符串数组中的最长公共前缀。

        如果不存在公共前缀，返回空字符串 ""。

        示例 1:

        输入: ["flower","flow","flight"]
        输出: "fl"

        """
        res_str = ""
        if len(strs) <= 0:
            res_str =  ""
        elif len(strs) == 1:
            res_str =  strs[0]
        else:
            s = strs.pop()  
            window = list()
            window_right = window_left = 0
            m_len = 0
            # 最长公共子序列
            s_pos = 0
            pos_len = 0
            while window_right<len(s):
                # 右滑
                c = s[window_right]
                
                window.append(c)
                sign =0 
                for ss in strs:
                    if window and ss and  window[0] == ss[0]   and "".join(window) in ss:
                        sign += 1
                
                if sign != (len(strs)):
                    break
                window_right += 1
            res_str = "" if window_left  == window_right else s[window_left:window_right]

        return res_str
#print(Solution().longestCommonPrefix(["ca","a"]))
    def longestCommonPrefix_eg(self, strs: list=[]) -> str:
        res=""
        # 按照最短的元素为基准将所有打包为元组
        for i in zip(*strs):
            if len(set(i))==1:
                res+=i[0]
            else:
                break 
        return res
#print(Solution().longestCommonPrefix_eg(["flower","flow","flight"]))

    def longestCommon(self, strs: list=[]) -> str:
        """
        编写一个函数来查找字符串数组中的最长公共前缀。

        如果不存在公共子串，返回空字符串 ""。

        示例 1:

        输入: ["flower","flow","flight"]
        输出: "fl"

        """
        res_str = ""
        if len(strs) <= 0:
            res_str =  ""
        elif len(strs) == 1:
            res_str =  strs[0]
        else:
            s = strs.pop()  
            window = list()
            window_right = window_left = 0
            m_len = 0
            # 最长公共子序列
            s_pos = 0
            pos_len = 0
            while window_right<len(s):
                # 右滑
           
                c = s[window_right]
                window_right += 1
                window.append(c)
                m_len += 1
                sign =0 
                for ss in strs:
                    if  "".join(window) in ss:
                        sign += 1
                if sign == (len(strs)):
                    if m_len > pos_len:
                        s_pos = window_left
                        pos_len = window_right - window_left
                else:
                    #左滑
                    while window_left < window_right:
                        c = s[window_left]
                        sign = 0
                        for ss in strs:
                            if  c in ss:
                                sign += 1
                        if sign != (len(strs)):
                            break
                        m_len -= 1
                        window[window_left]=''
                        window_left += 1
            res_str = "" if s_pos == pos_len else s[s_pos:(s_pos+pos_len)]
                   
        return res_str
#print(Solution().longestCommon(["flower","flow","flight"]))
#print(Solution().longestCommon(["ca","a"]))

    def lengthOfLongestSubstring(self, s: str) -> int:
        """“”“
        示例 1:

        输入: "abcabcbb"
        输出: 3 
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
        ”“”"""
        if len(s) <= 1:
            return len(s)
        window = dict()
        window_left = 0
        window_right = 0
        res_len = 0

        while window_right < len(s):
            c = s[window_right]
            window_right += 1

            if c in window:
                window[c] += 1
            else:
                window[c] = 1
       

            while window[c] > 1:
                x = s[window_left]
                
                window[x] -=1
                window_left += 1

            res_len = max(res_len,(window_right -window_left))

        return res_len
#print(Solution().lengthOfLongestSubstring("pwwkew"))

    def lengthOfLongestSubstring_offer(self, s: str) -> int:
        dic = {}
        max_length = 0
        cur_length = 0
        for i in range(len(s)):
            if s[i] not in dic or i - dic[s[i]] > cur_length:
                cur_length += 1
            else:
                cur_length = i - dic[s[i]]
            dic[s[i]] = i
            if max_length < cur_length:
                max_length = cur_length
        return max_length

#print(Solution().lengthOfLongestSubstring_offer("pwwkew"))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

        示例 1:

        输入：text1 = "abcde", text2 = "ace" 
        输出：3  
        解释：最长公共子序列是 "ace"，它的长度为 3。
        """
        if text1 is None or text2 is None:
            return 0
        if len(text1) <= 0 or len(text2) <= 0:
            return 0

        return len(set(text1)&set(text2))
#print(Solution().longestCommonSubsequence_sort("abcde","ace"))

    def longestCommonSubsequence_sort(self, text1: str, text2: str) -> int:
        """
        给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

        一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
        例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

        若这两个字符串没有公共子序列，则返回 0。

        

        示例 1:

        输入：text1 = "abcde", text2 = "ace" 
        输出：3  
        解释：最长公共子序列是 "ace"，它的长度为 3。
        """



print(Solution().longestCommonSubsequence_sort("abcde","ace"))