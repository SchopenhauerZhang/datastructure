class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
            小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

            如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

            请你计算 最多 能喝到多少瓶酒。

             

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/water-bottles
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            输入：numBottles = 9, numExchange = 3
            输出：13
            解释：你可以用 3 个空酒瓶兑换 1 瓶酒。
            所以最多能喝到 9 + 3 + 1 = 13 瓶酒。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/water-bottles
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if numBottles<=numExchange:
            return numBottles+1 if numBottles == numExchange else  numBottles
        _res = numBottles
        while numBottles >= numExchange:
            _res += numBottles//numExchange
            numBottles = numBottles// numExchange + numBottles%numExchange
            
        return _res 

    def _numWaterBottles_eg(self, numBottles: int, numExchange: int) -> int:
        sum=numBottles
        empty=numBottles
        m=empty//numExchange
        while m:
            empty=(empty%numExchange)+(m)
            sum=sum+m
            m=empty//numExchange
        return sum

print(Solution().numWaterBottles(9,3))#13
print(Solution().numWaterBottles(15,4))#19