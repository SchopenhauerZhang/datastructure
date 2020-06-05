
def package(wight_p:int,  nums:int, nums_w:list, nums_val:list):
    # import numpy
    # numpy.zeros([nums, wight_p])
    dp = [[0]*(wight_p+1) for i in range(nums+1)]

    for _n in range(1,nums+1):
        for _w in range(1,wight_p+1):
            if _w <  nums_w[_n -1]:
                dp[_n][_w] =  dp[_n-1][_w]
            else:
                dp[_n][_w] =  max(dp[_n-1][_w],dp[_n-1][_w-nums_w[_n-1]]+nums_val[_n-1])
            
    return dp[nums][wight_p]
# print(package(6,4,[1,2,3,0],[1,2,3,0]))
# 有一个背包，最大容量为 amount，有一系列物品 coins，每个物品的重量为
# coins[i]，每个物品的数量无限。请问有多少种方法，能够把背包恰好装满？

def perfect_package(coins:list=[],amount:int=1)->int:
    if amount <= 0:
        return 0
    if len(coins) == 0:
        return 0
    dp = [[0]* (amount+1) for i in range(len(coins)+1) ]
    for i in range(len(coins)+1):
        dp[i][0]=1

    for coin in range(1,len(coins)+1):
        for j in range(1,amount+1):
            if j-coins[coin-1]>=0:
                # 此前的组合+此后的组合
                dp[coin][j] = dp[coin-1][j]+dp[coin][j-coins[coin-1]]
            else:
                dp[coin][j] = dp[coin-1][j]
    print(dp)

    return dp[len(coins)][amount]
#print(perfect_package([1,2,5],5))

def perfect_package_m(coins:list=[],amount:int=1)->int:
    if amount <= 0:
        return 0
    if len(coins) == 0:
        return 0
    dp = [0 for i in range(amount+1)]
    dp[0] = 1

    for coin in range(0,len(coins)):
        for j in range(1,amount+1):
            if j - coins[coin]>=0:
                dp[j]=dp[j]+dp[j-coins[coin]]

    return dp[amount]
#print(perfect_package_m([1,2,5],5))

class Solution:

    def canPartition(self, nums: list=[]) -> bool:
        """
        给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

        注意:

        每个数组中的元素不会超过 100
        数组的大小不会超过 200
        示例 1:

        输入: [1, 5, 11, 5]

        输出: true

        解释: 数组可以分割成 [1, 5, 5] 和 [11].
        """
        if not nums:
            return False
        if sum(nums) %2!=0:
            return False
        dp = [[False]*(int(sum(nums))+1) for _ in range(0,len(nums)+1)]
        for i in range(1,len(nums)+1):
            dp[i][0] = True
        for i in range(1,len(nums)+1):#状态A
            for j in range(1,int(sum(nums)/2)+1):#状态B
                #择优
                if j - nums[i-1] >=0:
                    #放入
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
                  
                else:
                    #不放入
                    dp[i][j] = dp[i-1][j]
      
        return dp[len(nums)][int(sum(nums)/2)]
#print(Solution().canPartition([1, 5, 11, 5]))
 
    def _canPartition_(self, nums: list=[]) -> bool:
        """
        给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

        注意:

        每个数组中的元素不会超过 100
        数组的大小不会超过 200
        示例 1:

        输入: [1, 5, 11, 5]

        输出: true

        解释: 数组可以分割成 [1, 5, 5] 和 [11].
        """
        if not nums:
            return False
        if sum(nums) %2!=0:
            return False
        dp = [False for _ in range(int(sum(nums)/2+1))]
        dp[0] = True
     
        for i in range(1,len(nums)+1):#状态A
            j = sum(nums) // 2
            while j -nums[i-1] >= 0:
                #择优
                if j - nums[i-1] >=0:
                    #放入
                    dp[j] = dp[j] or dp[j-nums[i-1]]
                j -= 1
    
        return dp[int(sum(nums)/2)]
#print(Solution()._canPartition_([1, 5, 11, 5]))

    def dfs(self, nums, target, k):
        if 0==target:
            return True
        elif k<len(nums) and nums[k]>target:
            return False
        else:
            for i in range(k,len(nums)):
                if self.dfs(nums, target-nums[i], i+1):
                    return True
        return False
    
    def canPartition_(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums=sum(nums)
        if sums%2==1:
            return False
        nums=sorted(nums,key=lambda x:-x)
        target=sums//2
        return self.dfs(nums,target,0)
#print(Solution().canPartition_([1, 5, 11, 5]))

    def coinChange(self, coins: list, amount: int) -> int:
        """
        给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

        示例 1:

        输入: coins = [1, 2, 5], amount = 11
        输出: 3 
        解释: 11 = 5 + 5 + 1
        """
        if amount <0 :
            return -1
        if amount == 0:
            return 0
        if len(coins)<=0:
            return -1
        mem = dict()
        def dp(amt):
            if amt in mem:
                return mem[amt]
            if amt == 0:
                return 0
            if amt <0:
                return -1
            
            res = float('INF')
            for i in coins:
                sub = dp(amt-i)
                if sub == -1:continue
                res = min(res,1+sub)
            if res != float('INF'):
                mem[amt] = res
            else:
                mem[amt] = -1

            return mem[amt]
        
        return dp(amount)
#print(Solution().coinChange([1, 2, 5],100))

    def coinChange_(self, coins: list, amount: int) -> int:
        """
        示例 1:

        输入: coins = [1, 2, 5], amount = 11
        输出: 3 
        解释: 11 = 5 + 5 + 1
        """
        n = len(coins)
        coins = sorted(coins, reverse=True)
        res = amount + 1
        import math
        def dfs(index, target, count):
            nonlocal res
            this_coin = coins[index]
            if count + math.ceil(target/this_coin) >= res:
                return
            # 当前面额能否凑出target总数
            if target%this_coin == 0:
                res = count + target//this_coin
            
            if index == n-1:
                return
            
            for i in range(target//this_coin, -1 ,-1):
                dfs(index+1, target-i*this_coin, count+i)
        
        dfs(0, amount, 0)
        return -1 if res == amount+1 else res

    def Change(self, coins: list, amount: int) -> int:
        """
        给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额的硬笔组合数，没有返回0。
        每一种硬币有无限个。

        示例 1:

        输入: coins = [1, 2, 5], amount = 5
        输出: 4
        """
        dp = []
        for _ in range(amount+1):
            dp.append(0)
        dp[0] = 1

        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j - coins[i-1] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i-1]]
       

        return dp[amount]
#print(Solution().Change([1, 2, 5],5))

    def Change_better(self, coins: list, amount: int) -> int:
        """
        给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额的硬笔组合数，没有返回0。
        每一种硬币有无限个。

        示例 1:

        输入: coins = [1, 2, 5], amount = 5
        输出: 4
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for idx in range(amount - coin + 1):
                if dp[idx]:
                    dp[idx + coin] += dp[idx]
                    
        return dp[-1]

print(Solution().Change_better([1, 2, 5],5))








