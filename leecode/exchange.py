from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
            输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

             

            示例：

            输入：nums = [1,2,3,4]
            输出：[1,3,2,4] 
            注：[3,1,2,4] 也是正确的答案之一。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 1 :
            return nums 
        tmp = []
        for i in nums:
            if i%2 != 0:
                tmp.insert(0,i)
            else:
                tmp.append(i)
        return tmp

    def _exchange_eg(self, nums: List[int]) -> List[int]:
        oddIndex = len(nums) - 1
        cur = 0
        while cur < oddIndex:
            if nums[cur] % 2 == 0:
                nums[cur], nums[oddIndex] = nums[oddIndex], nums[cur]
                oddIndex -= 1
            else:
                cur += 1
        return nums