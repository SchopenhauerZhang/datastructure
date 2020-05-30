# -*- coding: UTF-8 -*-
import time
# 先看下题目：给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，再给一个总金额 amount，
# 问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。算法的函数签名如下：
# int coinChange(int[] coins, int amount);
class Coin(object):

    def coin_change(self, coins, amount):
        """
        暴力拆解
        """
        def dp(n):
            if n == 0 : return 0
            if n < 0 : return -1

            res = float("INF")
            for i in coins:
                subpro = dp(n-i)
                if subpro == -1 : continue
                res = min(res,1+subpro)

            return res if res!= float("INF") else -1

        return dp(amount)

    def coin_change_memorandum(self,coins, amount):
        """
        添加备忘录
        """
        mem = dict()
        def dp(n):
            if n in mem: return mem[n]
            if n ==0 :
                return 0
            elif n < -1:
                return  -1
            res = float("INF")
            for i in coins:
                subpro=dp(n-i)
                if subpro == -1:continue
                res = min(res,subpro+1)
            mem[n] = res  if res != float("INF") else -1

            return mem[n]

        return dp(amount)

print(Coin().coin_change([1,2,5],10))
print(Coin().coin_change_memorandum([1,2,5],10))