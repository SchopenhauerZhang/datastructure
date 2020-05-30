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
