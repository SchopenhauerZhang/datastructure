class Solution:
    def _convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        print(L)

        return ''.join(L)
    
    def convert(self, s: str, numRows: int) -> str:
        """
        将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
        ``
        比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

        L   C   I   R
        E T O E S I I G
        E   D   H   N
        之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

        请你实现这个将字符串进行指定行数变换的函数：

        string convert(string s, int numRows);
        示例 1:

        输入: s = "LEETCODEISHIRING", numRows = 3
        输出: "LCIRETOESIIGEDHN"
        示例 2:

        输入: s = "LEETCODEISHIRING", numRows = 4
        输出: "LDREOEIIECIHNTSG"

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/zigzag-conversion
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if len(s) <= numRows or numRows == 1:
            return s

        n = numRows
        index,sp,r = 0,1,0
        res = ['']*n
  
        while index<len(s):
            res[r] += s[index]
            if r == n-1:
                # rows退
                sp = -1
            if r == 0:
                # rows退进
                sp = 1
            r += sp
            index += 1 
        
        return ''.join(res)


#print(Solution().convert('LEETCODEISHIRING',3) == 'LCIRETOESIIGEDHN')
#print(Solution().convert('LEETCODEISHIRING',4) == 'LDREOEIIECIHNTSG')
#print(Solution().convert('AB',2) == 'AB')

    def _convert_eg(self, s: str, numRows: int) -> str:
        if numRows <2:
            return s
        grid = ['' for i in range(numRows)]
        cur = 0
        flag = -1
        for c in s:
            grid[cur]+= c
            if cur == 0 or cur == numRows-1:
                flag = -flag
            cur+=flag
        return "".join(grid)
