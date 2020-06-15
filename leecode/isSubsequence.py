class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

        你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

        字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

        示例 1:
        s = "abc", t = "ahbgdc"

        返回 true.

        示例 2:
        s = "axc", t = "ahbgdc"

        返回 false.

        后续挑战 :

        如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/is-subsequence
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _isSubsequence(self, s: str, t: str) -> bool:
        #双指针
        if s == t:
            return True

        if len(s) <= 0 :
            return True
            
        if len(t) <= 0:
            return False

        _s = 0 
        _t =0
        while _s < len(s) and _t < len(t):
            if s[_s] == t[_t]:
                _s += 1
            _t += 1

        return _s == len(s)
#print(Solution()._isSubsequence('abc',"ahbgdc"))

    def _isSubsequence_tree(self, s: str, t: str) -> bool:
        t_dict = dict()
        for k,v in enumerate(t):
            if v not in t_dict:
                t_dict[v] = []
            t_dict[v].append(k)

        def find(ll,index):
            high = len(ll)
            low = 0

            while low < high:
                mid = (low + high)//2
                if index > ll[mid]:
                    left = mid+1
                else:
                    high = mid
            return left

        _sign = 0
        for i in s:
            if not t_dict.get(i): 
                return False
            pos = find(t_dict[i],_sign)
            if pos == len(t_dict[i]):
                #没找到 
                return False
            _sign = t_dict[i][pos]+1
            
        return True
print(Solution()._isSubsequence('abc',"ahbgdc"))
