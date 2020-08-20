class Solution:
    def numTrees(self, n: int) -> int:
        """
            给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

            示例:

            输入: 3
            输出: 5
            解释:
            给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

            1         3     3      2      1
                \       /     /      / \      \
                3     2     1      1   3      2
                /     /       \                 \
            2     1         2                 3

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/unique-binary-search-trees
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not n or n<=2:
            return 0 if not n else n

        dp = [0]*n
        dp[0],dp[1] = 1,1
        # 卡塔兰数
        for i in range(2, n+1):
            for j in range(i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
    
    def _numTrees_eg(self, n: int) -> int:
        d=[-1 for i in range(n+1)]
        return self.f(n,d)
        
        
        
    def f(self,n,d):
        if d[n] != -1 :
            return d[n]
        if n <= 1 :
            return 1 
        s=0
        for i in range(1,n+1):
            s=s+ self.f(i-1,d)*self.f(n-i,d)
        d[n] =s 
        return s 