


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








