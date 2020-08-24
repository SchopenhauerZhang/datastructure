from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """
            从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

             

            示例 1:

            输入: [1,2,3,4,5]
            输出: True
             

            示例 2:

            输入: [0,0,1,2,5]
            输出: True
             

            限制：

            数组长度为 5 

            数组的数取值为 [0, 13] .

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        numbers = nums
        if len(numbers)!=5:
            return False
        king = 0
        numbers.sort()        
        for i,n in enumerate(numbers):
            if n == 0:
                king += 1
            elif i>0 and numbers[i-1]!=0:
                d = n - numbers[i-1]
                if d==0 or king<d-1:
                    return False
                king -= d-1                
        return True 
    
    def _isStraight_eg(self, nums: List[int]) -> bool:
        """
            精彩
        """
        count0 = 0
        nums.sort()
        # print(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
        maxVal = nums[-1]
        minVal = nums[count0]
        Non0 = []
        for i in nums[count0:]:
            if i not in Non0:
                Non0.append(i)
            else:
                return False
        if maxVal - minVal <= 4:
            return True
        else:
            return False