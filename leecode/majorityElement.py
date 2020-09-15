from typing import List
class Solution:
    def majorityElement(self, nums: list) -> int:
        """
        给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

        你可以假设数组是非空的，并且给定的数组总是存在多数元素。

         

        示例 1:

        输入: [3,2,3]
        输出: 3
        示例 2:

        输入: [2,2,1,1,1,2,2]
        输出: 2

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/majority-element
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        import collections
        counts = collections.Counter(nums)
        
        c = counts.most_common(1)
    
        return c[0][0]

# print(Solution().majorityElement([3,2,3]))
# print(Solution().majorityElement([2,2,1,1,1,2,2]))

    def _majorityElement_eg(self, nums: list) -> int:
        nums.sort()
        a = int(len(nums)/2)
        return nums[a]

    def _majorityElement_39(self, nums: List[int]) -> int:
        """
            数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

             

            你可以假设数组是非空的，并且给定的数组总是存在多数元素。

             

            示例 1:

            输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
            输出: 2
             

            限制：

            1 <= 数组长度 <= 50000

             

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if len(nums) <=2:
            return nums[-1] 
        return sorted(nums)[len(nums)//2]

#print(Solution()._majorityElement_eg([2,2,1,1,1,2,2]))

    def _majorityElement_17_10(self, nums: List[int]) -> int:
        """
            数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。
            示例 1：
            输入：[1,2,5,9,5,9,5,5,5]
            输出：5

            示例 2：

            输入：[3,2]
            输出：-1
            
            示例 3：

            输入：[2,2,1,1,1,2,2]
            输出：2
            说明：
            你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/find-majority-element-lcci
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) == 1:
            return -1 if not nums else nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] == nums[1] else -1
        num = sorted(nums,reverse=True)
        return num[len(nums)//2] if len(set(nums)) <= (len(nums)//2+1) else -1

    def _majorityElement_17_10_eg(self, nums: List[int]) -> int:
        """
             精彩
        """
        if nums is None:
            return -1
        nums.sort()
        mid=int(len(nums)/2)
        if nums.count(nums[mid])>int(len(nums)/2):
            return nums[mid]
        else:
            return -1
