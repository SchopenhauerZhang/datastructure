class Solution:
    def maxProfit(self, prices: list) -> int:
        """
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

        如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

        注意：你不能在买入股票前卖出股票。

         

        示例 1:

        输入: [7,1,5,3,6,4]
        输出: 5
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
            注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
        示例 2:

        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        if len(prices) == 1 or (len(prices) == 2 and prices[1]<=prices[0]):
            return 0 
        elif len(prices) == 2 and prices[1] >prices[0]:
            return prices[1] - prices[0]
        
        profit_d = float("-inf")
        profit_p = 0
        for i in range(len(prices)):
            profit_p = max(profit_p, profit_d+prices[i])
            profit_d = max(profit_d, -prices[i])
            
        return profit_p if profit_p else 0
#print(Solution()._maxProfit([7,1,5,3,6,4]))

    def _maxProfit_eg(self, prices: list) -> int:
        if not prices:
            return 0
        min_ = prices[0]
        res = 0
        for i in prices:
            if i < min_:
                min_ = i
            if i > min_:
                res = max(i - min_, res)
        return res

    def _maxProfit_(self, prices: list) -> int:
        """
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

         

        示例 1:

        输入: [7,1,5,3,6,4]
        输出: 7
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not prices:
            return 0

        profit = 0
        profit_p = float("-inf")
        
        for i in prices:
            tmp = profit
            profit = max(profit,profit_p+i)# 卖了
            profit_p = max(profit_p,tmp-i)#买了

        return profit if profit else 0
#print(Solution()._maxProfit_([7,1,5,3,6,4]))

    def _maxProfit__eg(self, prices: list) -> int:
        profit = 0
        lens = len(prices)
        for i in range(1, lens):
            j = prices[i] - prices[i-1] 
            if j > 0:
                profit += j
        return profit