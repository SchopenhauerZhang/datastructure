class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        """
         给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

        函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

        说明:

        返回的下标值（index1 和 index2）不是从零开始的。
        你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
        示例:

        输入: numbers = [2, 7, 11, 15], target = 9
        输出: [1,2]
        解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        l,r = 0,len(numbers)-1
        for r in range(len(numbers)-1,0,-1):
            tmp = target-numbers[r]
            if tmp < numbers[0]:
                continue
            l = 0
            while l < r:
                if numbers[l] == tmp:
                    break
                else:
                    l += 1
            if l < r:
                break

        return (l+1,r+1) if l < r  else (-1,-1)

# print(Solution().twoSum([2, 7, 11, 15],17))
# print(Solution().twoSum([2, 7, 11, 15],9))
# print(Solution().twoSum([0,0,3,4],0))
# print(Solution().twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997],542))

    def _twoSum(self, numbers: list, target: int) -> list:
        i = 0
        j = len(numbers)-1
        while j>i:
            if numbers[i]+numbers[j]==target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1;
            else:
                j-=1
        return []
