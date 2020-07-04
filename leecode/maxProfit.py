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

    def _maxProfit___(self, prices: list) -> int:
        """"
            给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
            设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

            你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
            卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
            示例:

            输入: [1,2,3,0,2]
            输出: 3 
            解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        
        


        return 1

#print(Solution()._maxProfit___([1,2,3,0,2]))
#print(Solution()._maxProfit___([1,2,4]))
#print(Solution()._maxProfit___([1,2,3,0,2]))

    def _maxProfit__2(self, prices: list) -> int:
        """
        给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

        设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

        注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

        示例 1:

        输入: [3,3,5,0,0,3,1,4]
        输出: 6
        解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
             随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
        示例 2:

        输入: [1,2,3,4,5]
        输出: 4
        解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
             注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
             因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
        示例 3:

        输入: [7,6,4,3,1] 
        输出: 0 
        解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _maxProfit__k(self, prices: list) -> int:
        dp_i_0 = 0 
        dp_i_1 = float("-inf") 

        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1,-prices[i])
        
        return dp_i_0 if dp_i_0 else 0
#print(Solution()._maxProfit__k([3,3,5,0,0,3,1,4]))

    def _maxProfit__with_cool(self, prices: list) -> int:
        """
        给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

        设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

        你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
        示例:

        输入: [1,2,3,0,2]
        输出: 3 
        解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not prices or len(prices) <1:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        dp_i_2 = 0
        
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1,dp_i_2-prices[i])
            dp_i_2 = tmp

        return dp_i_0
#print(Solution()._maxProfit__with_cool([1,2,3,0,2]))

    def _maxProfit__with_free(self, prices: list,fee: int) -> int:
        """
        手续费
        def maxProfit(self, prices: List[int], fee: int) -> int:

        输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
        输出: 8
        解释: 能够达到的最大利润:  
        在此处买入 prices[0] = 1
        在此处卖出 prices[3] = 8
        在此处买入 prices[4] = 4
        在此处卖出 prices[5] = 9
        总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not prices or len(prices) <2:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        
        for price in prices:
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1+price)
            dp_i_1 = max(dp_i_1,tmp-fee-price)

        return dp_i_0
#print(Solution()._maxProfit__with_free([1, 3, 2, 8, 4, 9],2))

    def _maxProfit__with_free_eg(self, prices: list,fee: int) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        buy = sold = prices[0]
        for price in prices[1:]:
            # if current price is higher than sold, 
            # then we will consider this new price as sold price
            if price >= sold:
                sold = price

            # if current price is lower than sold, 
            # then we may think sold the stock at "sold price"
            else:
                gain = sold - buy - fee
                # we will perform a transmission only if
                # 1. we can earn money, and
                # 2. gain is large enough to pay “opportunity cost”, because
                #       if we perform transmission, the new buying price may be higher than
                #       current buying price, and the difference is the opportunity cost. eg.
                #       prices are [1, 5, 4, 10] with fee = 3,
                #       if we sold the stock at 5, then we cannot
                #       get a higher profit with "buy at 1 sold at 10"
                if gain > 0 and gain > price - buy:
                    profit += gain
                    buy = sold = price
                # if we cannot earn any profit, 
                # then we should rethink changing the buying price
                elif price < buy:
                    buy = sold = price
        if sold - buy > fee:
            profit += sold - buy - fee
        return profit

    def _maxProfit_k(self, prices: list, k: int) -> int:
        




print(Solution()._maxProfit_k([3,2,6,5,0,3],2))