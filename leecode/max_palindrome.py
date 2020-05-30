class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        最长回文字符串
        """
        target = dict()
        for i in s:
            if i in target:
                target[i] += 1 
            else:
                target[i] = 1

        window = dict()
        relt = str()
        window_right = window_left = 0
        # 最长子序列
        s_pos = 0
        pos_len = 0

        m_len = 0
        
        while window_right<len(s):
            # 右滑
            c = s[window_right]
            window_right += 1
            if c in window:
                window[c] += 1 
            else:
                window[c] = 1
     
            if window[c] == target[c]:
                m_len += 1

            while m_len < window_right-window_left:
                #左滑
                c = s[window_left]
                if c in window and window[c] == target[c]:
                    m_len -= 1
                    window[c] -= 1
                else:
                    if m_len > pos_len:
                        s_pos = window_left
                        pos_len = m_len
                
                window_left += 1

        return s[s_pos:(s_pos+pos_len)]

print(Solution().longestPalindrome('cbbd'))



