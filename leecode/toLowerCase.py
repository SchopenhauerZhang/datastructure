class Solution:
    def toLowerCase(self, str: str) -> str:
        """
            实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

 

            示例 1：

            输入: "Hello"
            输出: "hello"
            示例 2：

            输入: "here"
            输出: "here"
            示例 3：

            输入: "LOVELY"
            输出: "lovely"

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/to-lower-case
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not str or not str.strip():
            return ''
        res = ''
        for i in list(str):
            if  65 <= ord(i) <= 90:
                res+= chr(ord(i) + 32)
            else:
                res+= i
        return res
    
    def _toLowerCase_eg_1(self, str: str) -> str:
        res=''
        for c in str:            
            if 65<=ord(c)<=90:
                c=chr(ord(c)+32)
                # print(c)
            res+=c
        return res

    def _toLowerCase_eg_2(self, str: str) -> str:
        if str==None:
            return None
        if str=="":
            return ""

        low=[chr(i) for i in range(97, 123)]
        upp=[chr(i) for i in range(65, 91)]

        lis=list(str)
        for i in range(len(lis)):
            if lis[i] in upp:
                lis[i]=low[upp.index(lis[i])]

        return "".join(lis)