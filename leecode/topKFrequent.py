from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

             

            示例 1:

            输入: nums = [1,1,1,2,2,3], k = 2
            输出: [1,2]
            示例 2:

            输入: nums = [1], k = 1
            输出: [1]
             

            提示：

            你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
            你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
            题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/top-k-frequent-elements
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
    
        if not nums or k is None or k == 0 or len(nums) == 1:
            if len(nums) == 1:
                return nums
            return [] 
        if len(set(nums)) <= k :
            return list(set(nums))
        from collections import Counter
        num = Counter(nums)
        sort_num = sorted(num.items(),key=lambda x : x[1])
        res = [x for x,y in sort_num[::-1][:k]]
        return res

    def _topKFrequent_eg(self, nums: List[int], k: int) -> List[int]:
        """
            精彩
        """
        return [i[0] for i in Counter(nums).most_common(k)]