class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        给你两个二进制字符串，返回它们的和（用二进制表示）。

        输入为 非空 字符串且只包含数字 1 和 0。

         

        示例 1:

        输入: a = "11", b = "1"
        输出: "100"
        示例 2:

        输入: a = "1010", b = "1011"
        输出: "10101"

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/add-binary
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        res = ''
        incre = 0
        
        a ,b = (str('0'*(len(b)-len(a)))+a ,b) if len(a) < len(b) else (a,str('0'*(len(a)-len(b)))+b) 
        a = list(a)
        b = list(b)
       
        for i in range(max(len(a),len(b))-1,-1,-1):
            _b = 0
            _a = 0
            if i < len(a):
                _a = a[i] 
            if i < len(b):
                _b = b[i]
            
            incre = int(_b) + int(_a) + incre 
            res = str(incre)+res if incre < 2 else str(incre-2)+res
            incre = 0 if incre < 2 else incre//2
         
        if incre :
            res = str(incre)+res
        return res

# print(Solution().addBinary('10','10'))
# print(Solution().addBinary('10','110'))

    def _addBinary_eg(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y #保存当前结果，若位不相同，等于1，若位相同，则等于0
            carry = (x & y) << 1 #保存进位结果
            x, y = answer, carry
        return bin(x)[2:]