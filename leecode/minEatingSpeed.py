
class Solution:
    def minEatingSpeed(self, piles: list, H: int) -> int:
        """
        珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

        珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

        珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

        返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
        示例 1：

        输入: piles = [3,6,7,11], H = 8
        输出: 4
        """
        if H <= 0 :
            return 0
        if len(piles)<1:
            return 0

        def is_e(index):
            count = 0
            for i in piles:
                count += i//index +(1 if i%index>0 else 0)
                    
            return count <= H

        left =1
        right = max(piles)+1

        while left < right:
            mid = left+(right-left)//2
            #print(str(left)+":"+str(right)+":"+str(mid))
            if is_e(mid):
                right = mid
            else:
                left = mid+1

        return left

#print(Solution().minEatingSpeed([30, 11, 23, 4, 20],5))
    def _minEatingSpeed_better(self, piles: list, H: int) -> int:
        import math
        def eatcost(piles, m):
            rst=0
            for i in piles:
                rst=math.ceil(i/m)+rst
            return rst
        if len(piles)==H:
            return max(piles)
        else :
            mink = math.ceil(sum(piles)/H)
            maxk = min(max(piles),math.ceil((sum(piles)-len(piles))/(H-len(piles))))
        while mink<maxk:
            midk=(mink+maxk)//2
            if eatcost(piles,midk)<=H:
                maxk=midk
            else:
                mink=midk+1
        return mink

    def shipWithinDays(self, weights: list, D: int) -> int:
        """
        传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
        传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

        返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
        示例 1：

        输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
        输出：15
        解释：
        船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
        第 1 天：1, 2, 3, 4, 5
        第 2 天：6, 7
        第 3 天：8
        第 4 天：9
        第 5 天：10

        请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
        """
        def is_load(_load):
            x = _load
            j = 0
            # for i in weights:
            #     if _load - i <=0:
            #         j += 1
            #         if _load -i < 0 :
            #             _load = x -i
            #         else:
            #             _load = x
            #     else:
            #         _load -= i 
            for i in range(0,D):
                _load = x
                while _load - weights[j] >= 0:
                    _load -= weights[j]
                    j +=1
                    if j == len(weights):
                        return True
            return False
            
        left = 1
        right = sum(weights)+1
        while left < right:
            mid = left + (right-left) //2
            if is_load(mid):
                right = mid
            else:
                left = mid+1

        return left

#print(Solution().shipWithinDays([3,2,2,4,1,4],3))
    def _shipWithinDays_better(self, weights:list, D: int) -> int:
        def can_ship(K):
            left, d = 0, 0
            for weight in weights:
                if left < weight:
                    d += 1
                    left = K
                left -= weight
            return d <= D
        lo = max(weights)
        hi = max(weights) * len(weights) // D + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if not can_ship(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
