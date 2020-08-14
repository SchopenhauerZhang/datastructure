class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
            给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not pattern:
            return False
        strs = str
        _strs = strs.split(' ')
        patterns = list(pattern)
        if len(set(patterns)) != len(set(_strs)) or len(patterns)!= len(_strs):
            return False

        _tuple = [i for i in zip( _strs,patterns )]
        l,r,pre_l,pre_r = 0,len(_tuple)-1,None,None
        while l <= r:
            
            
            if _tuple[l][0] == pre_l and _tuple[l][1] == pre_r:
                pass
            elif _tuple[l][0] != pre_l and _tuple[l][1] != pre_r:
                pass
            else:
                return False
            if _tuple[r][0] == _tuple[l][0] and _tuple[r][1] == _tuple[l][1]:
                pass
            elif _tuple[r][0] != _tuple[l][0] and _tuple[r][1] != _tuple[l][1]:
                pass
            else:
                return False

            pre_l,pre_r = _tuple[l]
            l += 1
            r -= 1
    
        return True

    def _wordPattern_eg(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        hashMap = {}
        mapVal = {}
        for i in range(len(pattern)):
            if pattern[i] in hashMap:
                if hashMap[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in mapVal:
                    return False
                hashMap[pattern[i]] = words[i]
                mapVal[words[i]] = 1
        return True

#print(Solution().wordPattern('aba',"dog dog cat"))
#print(Solution().wordPattern('abaaa',"dog cat cat dog dog"))
