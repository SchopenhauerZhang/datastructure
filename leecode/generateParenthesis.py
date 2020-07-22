class Solution:
    def generateParenthesis(self, n: int) -> list:
        """
        数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

        示例：

        输入：n = 3
        输出：[
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
            ]
        通过次数151,783提交次数200,187

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/generate-parentheses
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        res = []
        left = n
        right = n
        strs = ''
        self.generate(left,right,strs,res)
        for i in res:
            print(i)
        return res
    
    def generate(self,l,r,s,res):
        if l < 0 or r < 0 or l > r:
            return 
        if l == 0 and r== 0:
            res.append(s)
            return 
         
        s+='('
        self.generate(l-1,r,s,res)
        # if ress:
        #     res.append(ress)
        s = s[:len(s)-1]

        s+=')'
        self.generate(l,r-1,s,res)
        # if ress:
        #     res.append(ress)
        s = s[:len(s)-1]
        #return res

#print(Solution().generateParenthesis(3))

    def _generateParenthesis_eg(self, n: int) -> list:
        ans = []
        def backtrack(s,left,right):
            if len(s)==2*n:
                ans.append(''.join(s))
                #return ans
            if left < n:
                s.append('(')
                backtrack(s,left+1,right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s,left,right+1)
                s.pop()
        backtrack([],0,0)
        return ans