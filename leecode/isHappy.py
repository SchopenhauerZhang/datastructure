class Solution:
    def isHappy(self, n: int) -> bool:
        """
            编写一个算法来判断一个数 n 是不是快乐数。

            「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

            如果 n 是快乐数就返回 True ；不是，则返回 False 。

             

            示例：

            输入：19
            输出：true
            解释：
            12 + 92 = 82
            82 + 22 = 68
            62 + 82 = 100
            12 + 02 + 02 = 1

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/happy-number
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not n or n == 1:
            return  True if n == 1 else False
        _sum = 0
        res = []
        while True:
            _sum = 0
            for i in str(n):
                _sum += int(i)**2
           
            if _sum == 1:
                return True
            else:
                n = _sum
                if _sum not in res:
                    res.append(_sum)
                else:
                    return False
    def _isHappy_eg(self, n: int) -> bool:
        if n<10:
            if n==1 or n==7:
                return True
            else:
                return False
        ans=0
        while n:
            ans+=(n%10)**2
            n=n//10
        return self.isHappy(ans)