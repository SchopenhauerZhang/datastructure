class Solution:
    def _reverseWords(self, s: str) -> str:
        res = ''
        for i in s.split(' '):
            res += ''.join(i[::-1])+' '
        return res
    def reverseWords(self, s: str) -> str:
        """
            输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

             

            示例 1：

            输入: "the sky is blue"
            输出: "blue is sky the"
            示例 2：

            输入: "  hello world!  "
            输出: "world! hello"
            解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
            示例 3：

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        
        return ' '.join([i for i in s.split(' ')[::-1] if i.strip()] ).strip()
    
    def _reverseWords_eg(self, s: str) -> str:
        tokens = s.strip().split()
        tokens.reverse()
        return ' '.join(tokens)


# print(Solution().reverseWords("a good   example"))
