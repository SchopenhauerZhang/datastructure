class Solution:
    def countPrimes(self, n: int) -> int:
        """
        统计所有小于非负整数 n 的质数的数量。

        示例:

        输入: 10
        输出: 4
        解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
        """


        arr = [True] * (n+1)
  
        i = 2
        if n <= 2:
            return 0
        
        def is_p(x):
            for j in range(2,x):
                
                if x%j ==0:
                    return False
            return True
            
        while i*i < n:
            
            if is_p(i):
                
                xx = i*i
                while xx < n:
                    
                    arr[xx] = False
                    
                    xx += i
            
            i += 1
        count = 0
        
        for i in range(0,n):
            if arr[i]:
                count += 1
    
        return count-1-1

print(Solution().countPrimes(3))