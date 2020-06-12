class Solution:
    def isValid(self, s: str) -> bool:
        """
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

        有效字符串需满足：

        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。

        示例 1:

        输入: "()"
        输出: true
        示例 2:

        输入: "()[]{}"
        输出: true
        示例 3:

        输入: "(]"
        输出: false

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/valid-parentheses
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _isValid(self, s: str) -> bool:
        if len(s) <= 0:
            return True
        if len(s)==1:
            return False

        stack = list()
        def is_v(c,v):
            if c==')':
                return v == '('
            elif c=='}':
                return v == '{'
            elif c==']':
                return v == '['
            return False

        for i in s:
            if i in ('(','{','['):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if not is_v(i,stack[len(stack)-1]):
                    return False
                else:
                    stack.pop()
        if len(stack) ==0:
            return True

        return False
# print(Solution()._isValid(")}"))
# print(Solution()._isValid("{[]}"))

    def _isValid_eg(self, s: str) -> bool:
        match_dict={'(':')','{':'}','[':']','?':'?'}
        stack=['?']
        for i in s:
            if i in match_dict:stack.append(i)
            elif match_dict[stack.pop()]!=i:return False
        return len(stack)==1

