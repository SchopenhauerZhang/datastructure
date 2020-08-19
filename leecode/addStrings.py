class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
            给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

             

            提示：

            num1 和num2 的长度都小于 5100
            num1 和num2 都只包含数字 0-9
            num1 和num2 都不包含任何前导零
            你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/add-strings
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not num1 or not num2 or num1 == '0' or num2=='0':
            return num1 if not num2 or num2 == '0' else num2
        if len(num1) == 1 or len(num2) == 1:
            if len(num1) == 1:
                _s = 0
                _s = _s + int(list(num2)[::-1][0]) + int(num1)
                res = str(_s%10)
                _s = int(_s //10)
                for i in list(num2)[::-1][1:]:
                    _s = _s + int(i) 
                    res = str(_s%10)+res
                    _s = int(_s //10)
                
                return str(_s)+res if _s != 0 else res
            elif  len(num2) == 1:
                _s = 0
                _s = _s + int(list(num1)[::-1][0]) + int(num2)
                res = str(_s%10)
                _s = int(_s //10)
                for i in list(num1)[::-1][1:]:
                    _s = _s + int(i) 
                    res = str(_s%10)+res
                    _s = int(_s //10)
                return str(_s)+res if _s != 0 else res
        _min = min(len(num1),len(num2))
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        _i = 0
        _flag = 0
        res = ''
        while _i < _min:
            
            _sum = int(num1[_i])+int(num2[_i])+_flag
            _flag,_sum = int(_sum//10), _sum%10
            res  = str(_sum)+res
            _i += 1
        
        if len(num1) > _min:
            _s = 0
            _s = _s + int(num1[_min:][0]) + int(_flag)
            res = str(_s%10)+res
            _s = int(_s //10)
            print(res,_s)
            if len(num1[_min:]) == 2:
                return str((int(num1[_min:][1]) + _s))+res 
            for i in num1[_min:][1:]:
                _s = _s + int(i) 
                res = str(_s%10)+res
                _s = int(_s //10)
            return str(_s)+res if _s != 0 else res
        elif len(num2) > _min:
            _s = 0
            _s = _s + int(num2[_min:][0]) + int(_flag)
            res = str(_s%10)+res
            _s = int(_s //10)
            if len(num1[_min:][::-1]) == 2:
                return str((int(num1[_min:][1]) + _s))+res 
            for i in num2[_min:][1:]:
                _s = _s + int(i) 
                res = str(_s%10)+res
                _s = int(_s //10)
            return str(_s)+res if _s != 0 else res
        else:
            return str(_flag)+res if _flag != 0 else res

    def _addStrings_eg(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
    def _addStrings_eg_1(self, nums1: str, nums2: str) -> str:
        """
            精彩
        """

        nums1 = nums1[::-1]
        nums2 = nums2[::-1]
        c = 0
        res = ""
        for i in range(min(len(nums1),len(nums2))):
            d = (c + int(nums1[i]) + int(nums2[i]))%10
            res += str(d)
            c = (c + int(nums1[i]) + int(nums2[i]))//10
        if len(nums1) > len(nums2):
            for i in range(min(len(nums1),len(nums2)),len(nums1)):
                d = (c+int(nums1[i]))%10
                res += str((d)%10)
                c = (c+int(nums1[i]))//10
        else:
            for i in range(min(len(nums1),len(nums2)),len(nums2)):
                d = (c+int(nums2[i]))%10
                res += str((d)%10)
                c = (c+int(nums2[i]))//10
        return res[::-1] if not c else str(c) + res[::-1]
        
            
        
        