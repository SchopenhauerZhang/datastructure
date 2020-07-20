class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

        示例：

        输入: S = "ADOBECODEBANC", T = "ABC"
        输出: "BANC"
        说明：

        如果 S 中不存这样的子串，则返回空字符串 ""。
        如果 S 中存在这样的子串，我们保证它是唯一的答案。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/minimum-window-substring
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not t: return ''
        d,dd,i,j,n={},{},0,0,len(s)
        for c in t: d[c]=d.get(c,0)+1
        for i in range(len(s)):
            c=s[i]
            if c in d:
                d[c]-=1
                if not d[c]: del d[c]
                if not d:
                    k,l,i=0,i+1,i+1
                    break
            else: dd[c]=dd.get(c,0)+1
        if d: return ''
        while i<n:
            if not d:
                if i-j<l: k,l=j,i-j
                c,j=s[j],j+1
                if c in dd:
                    dd[c]-=1
                    if not dd[c]: del dd[c]
                else: d[c]=1
            else:
                c,i=s[i],i+1
                if c in d:
                    d[c]-=1
                    if not d[c]: del d[c]
                else: dd[c]=dd.get(c,0)+1
        while not d:
            if i-j<l: k,l=j,i-j
            c,j=s[j],j+1
            if c in dd:
                dd[c]-=1
                if not dd[c]: del dd[c]
            else: d[c]=1
        return s[k:k+l]
        
# https://leetcode-cn.com/problems/minimum-window-substring/submissions/
# print(Solution().minWindow("bbaa",  "aba"))
# print(Solution().minWindow("ADOBECODEBANC",  "ABC"))
# print(Solution().minWindow("abc",  "ac"))
# print(Solution().minWindow("ABC",  "B"))

    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            # 找可行窗口
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                # 缩小可行窗口
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res
