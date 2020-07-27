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

        
print(Solution()._majorityElement_eg([2,2,1,1,1,2,2]))