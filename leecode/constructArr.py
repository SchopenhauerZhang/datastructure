from typing import List
class Solution:
    def constructArr(self, A: List[int]) -> List[int]:
        """
        给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

         

        示例:

        输入: [1,2,3,4,5]
        输出: [120,60,40,30,24]
         

        提示：

        所有元素乘积之和不会溢出 32 位整数
        a.length <= 100000
        通过次数22,344提交次数38,167

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            2个for循环更快？
        """

        ans = []
        _len = len(A)
        prod = 1
        for i in range(_len):
            ans.append(prod)
            prod *= A[i]
        prod = 1
        for i in range(len(A) - 1, -1, -1):
            ans[i] *= prod
            prod *= A[i]
        return ans
    
    def _constructArr_eg(self, a: List[int]) -> List[int]:
        if not a:
            return []
        res = [] 
        sumValue = 1 
        sumWithZero =1 
        zeroCount = 0 
        for i in range(len(a)):
            sumValue *=a[i]
            if a[i]==0:
                zeroCount+=1
            else:
                sumWithZero *=a[i]
        if zeroCount>1:
            return [0]*(len(a))
        elif zeroCount ==1:
            for i in range(len(a)):
                if a[i]==0:
                    res.append(sumWithZero)
                else:
                    res.append(0)
            return res 
        else:
            for i in range(len(a)):
                res.append(sumValue//a[i])
            return res 