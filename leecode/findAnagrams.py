class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
            给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

            字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

            说明：

            字母异位词指字母相同，但排列不同的字符串。
            不考虑答案输出的顺序。
            示例 1:

            输入:
            s: "cbaebabacd" p: "abc"

            输出:
            [0, 6]

            解释:
            起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
            起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
             示例 2:

            输入:
            s: "abab" p: "ab"

            输出:
            [0, 1, 2]

            解释:
            起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
            起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
            起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            超出时间限制
        """
        if not p or not s :
            if not p or not s :
                return []
        if len(s) < len(p):
            return []
        def requal(l,r):
            if len(l) != len(r):
                return False
            l,r= list(l),list(r)
            for i in l:
                if i in r:
                    del r[r.index(i)]
            return True if not r else False
        ll = len(s)
        _ll = len(p)
        res = []
        for i in range(ll):
            if i+_ll>ll:
                continue
            if requal(s[i:_ll+i],p):
                res.append(i)
        return res
    
    def _findAnagrams_eg(self, s: str, p: str) -> list:
        '''
        解法1：滑动窗口
        '''
        res = []
        window = {}
        needs = {}
        for c in p:
            needs[c] = needs.get(c, 0) + 1
        left, right = 0, 0
        length, limit = len(p), len(s)
        while right < limit:
            c = s[right]
            if c not in needs:
                window.clear()
                right = right + 1
                left = right
            else:
                window[c] = window.get(c, 0) + 1
                if length == right - left + 1:
                    if window == needs:
                        res.append(left)
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return res