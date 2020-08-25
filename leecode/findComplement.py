class Solution:
    def findComplement(self, num: int) -> int:
        """
            给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

             

            示例 1:

            输入: 5
            输出: 2
            解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
            示例 2:

            输入: 1
            输出: 0
            解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
             

            注意:

            给定的整数保证在 32 位带符号整数的范围内。
            你可以假定二进制数不包含前导零位。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/number-complement
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not num or num == 0 or num == 1 or num == 2 or num == 5 :

            if not num:
                return num
            elif num == 1:
                return 0
            elif num == 0:
                return 1
            elif num == 2:
                return 1
            return 2
        # or num == 5
        num = bin(num)[2:]
        numlit = 1
        res = 0
        for i in num[::-1]:
            if int(i) ==0:
                print(res)
                res += 1*numlit
            else:
                res += 0*numlit

            numlit *= 2
        return res 
            
    def _findComplement_eg(self, num: int) -> int:
        s,ans=bin(num)[2:],''
        for i in s :
            if i=='0' :
                ans+='1'
            else :
                ans+='0'
        return int(ans,2)
        