class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """
            给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。

            从形式上讲，只有满足下面几点之一，括号字符串才是有效的：

            它是一个空字符串，或者
            它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
            它可以被写作 (A)，其中 A 是有效字符串。
            给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

             

            示例 1：

            输入："())"
            输出：1
            示例 2：

            输入："((("
            输出：3
            示例 3：

            输入："()"
            输出：0
            示例 4：

            输入："()))(("
            输出：4
             

            提示：

            S.length <= 1000
            S 只包含 '(' 和 ')' 字符。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not S or len(S) == 1:
            return 0 if not S else 1
        q = []
        for i in S:
            if not q:
                q.append(i)
            else:
                if i == '(':
                    q.append(i)
                    continue
                else:
                    if q[-1] == '(':
                        q.pop()
                        continue
                q.append(i)
        return len(q)
    
    def minAddToMakeValid_eg(self, S: str) -> int:
        left = right = 0
        #for i in range(len(S)):
        for s in S:
            if s == '(':
                left += 1
            if s == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left+right 