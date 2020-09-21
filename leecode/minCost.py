from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        """
            给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。

            返回使字符串任意相邻两个字母不相同的最小删除成本。

            请注意，删除一个字符后，删除其他字符的成本不会改变。

             

            示例 1：

            输入：s = "abaac", cost = [1,2,3,4,5]
            输出：3
            解释：删除字母 "a" 的成本为 3，然后得到 "abac"（字符串中相邻两个字母不相同）。
            示例 2：

            输入：s = "abc", cost = [1,2,3]
            输出：0
            解释：无需删除任何字母，因为字符串中不存在相邻两个字母相同的情况。
            示例 3：

            输入：s = "aabaa", cost = [1,2,3,4,1]
            输出：2
            解释：删除第一个和最后一个字母，得到字符串 ("aba") 。
             

            提示：

            s.length == cost.length
            1 <= s.length, cost.length <= 10^5
            1 <= cost[i] <= 10^4
            s 中只含有小写英文字母

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/minimum-deletion-cost-to-avoid-repeating-letters
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s or len(s) == 1:
            return 0
        if len(s) == 2:
            return 0 if s[0] != s[1] else min(cost)
        q = []
        ll = len(s)
        res = 0
        for i in range(ll):
            if not q:
                q.append(i)
            else:
                if s[i] == s[q[-1]]:
                    _res = min(cost[i],cost[q[-1]])
                    res += _res
                    q[-1] = q[-1] if _res == cost[i] else i
                else:
                    q.append(i)
     
        return res
    
    def minCost_eg(self, s: str, cost: List[int]) -> int:
        if len(s)==0 or len(s)==1:

            return 0
        elif len(set(s))==1:
            return sum(cost)-max(cost)
        price=0
        m=0
        for i in range(1,len(s)):
            now=0
            if s[i]==s[m]:
                now=min(cost[i],cost[m])
        
                if cost[i]>cost[m]:
                    m=i
                
                price+=now
            else:
                m=i
                
            
        return price

