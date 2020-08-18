from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
            一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。

            给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。

            如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

            请注意：

            石子的数量 ≥ 2 且 < 1100；
            每一个石子的位置序号都是一个非负整数，且其 < 231；
            第一个石子的位置永远是0。
            示例 1:

            [0,1,3,5,6,8,12,17]

            总共有8个石子。
            第一个石子处于序号为0的单元格的位置, 第二个石子处于序号为1的单元格的位置,
            第三个石子在序号为3的单元格的位置， 以此定义整个数组...
            最后一个石子处于序号为17的单元格的位置。

            返回 true。即青蛙可以成功过河，按照如下方案跳跃： 
            跳1个单位到第2块石子, 然后跳2个单位到第3块石子, 接着 
            跳2个单位到第4块石子, 然后跳3个单位到第6块石子, 
            跳4个单位到第7块石子, 最后，跳5个单位到第8个石子（即最后一块石子）。
            示例 2:

            [0,1,2,3,4,8,9,11]

            返回 false。青蛙没有办法过河。 
            这是因为第5和第6个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/frog-jump
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            超出时间限制
        """
        if not stones:
            return False
        if stones[-1]+1 >= 2**31 or stones[0]  != 0 or len(stones) < 2 or len(stones) >= 1100 :
            
            return False
        dp = [0] * (stones[-1]+1)
        max_r = stones[-1]
        for i in stones:
            dp[i] = 1
        
        def cross(dp,k,i):
            
            nonlocal max_r
            if i ==  max_r:
                return True
            elif i >  max_r:
                return False

            if i == 0:
                k = 1
            elif dp[i] == 0:
                return False
            else:
                if k-1>=1:
                    return cross(dp,k,i+k) or cross(dp,k-1,i+k-1) or cross(dp,k+1,i+k+1)
                return cross(dp,k,i+k) or cross(dp,k+1,i+k+1)
            i += k
            return cross(dp,k,i)

        return cross(dp,0,0)

    def _canCross_(self, stones: List[int]) -> bool:
        """
        精彩
        """
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True
        for i in range(1, n):
            for j in range(i):
                diff = stones[i] - stones[j]
                # print(i, diff)
                if diff < 0 or diff >= n or not dp[j][diff]: continue
                
                dp[i][diff] = True
                if diff - 1 >= 0: dp[i][diff - 1] = True
                if diff + 1 < n: dp[i][diff + 1] = True
        
        
        return any(dp[-1])

    def _canCross_eg(self, stones: List[int]) -> bool:
        # #dp[i], 最后一次跳到 i position需要的步长
        # #if dp[i] == []:没法跳到 i position
        # #for j < i, interval = stones[i] - stones[j]
        # #if interval belongs to dp[j], dp[i].add(interval+-1)
        # #???: list快还是set快？
        # dp = collections.defaultdict(set)
        # dp[0]=set([1])
        # for i in range(1,len(stones)):
        #     for j in range(i):
        #         interval = stones[i]-stones[j]
        #         if interval in dp[j]:
        #             if interval-1>0:
        #                 dp[i] = dp[i]|set([interval,interval-1,interval+1])
        #             else:
        #                 dp[i] = dp[i]|set([interval,interval+1])
        # if dp[len(stones)-1]:return True
        # return False
        
        #DFS, TLE???
        #i: current position
        return dfs(stones,1,dic,len(stones),1,memo)
        def dfs(stones,i,dic,l,jump,memo):
            if i==l-1:return True
            if (i,jump) in memo:
                return False
            if jump-1>0:
                choices = (jump+1,jump,jump-1)
            else:
                choices = (jump+1,jump)
            for j in choices:
                cur = j+stones[i]
                if cur in dic:
                    if dfs(stones,dic[cur],dic,l,j,memo):
                        return True
                    memo[(dic[cur],j)]=False
            memo[(i,jump)]=False
            return False
        
        dic = {};memo={}
        for i in range(len(stones)):
            dic[stones[i]] = i
            if i >0 and stones[i]-stones[i-1]>i:
                return False
        print(dic)
        return dfs(stones,1,dic,len(stones),1,memo)
#print(Solution().canCross([0,1,3,5,6,8,12,17]))
#print(Solution().canCross([0,1,2,3,4,8,9,11]))
#print(Solution().canCross([0,1,3,4,5,7,9,10,12]))
print(Solution()._canCross_eg([0,1,3,6,10,15,21,28]))


