from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """
            输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

             

            示例 1:

            输入: [10,2]
            输出: "102"
            示例 2:

            输入: [3,30,34,5,9]
            输出: "3033459"
             

            提示:

            0 < nums.length <= 100
            说明:

            输出结果可能非常大，所以你需要返回一个字符串而不是整数
            拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        # write code here
        if not numbers:
            return ""
        arr = list(str(x) for x in numbers)
        def f(a,b):
            if a+b<b+a:
                return -1
            else:
                return 1
        arr.sort(key=functools.cmp_to_key(f))
        return "".join(arr)
    
    def _minNumber_eg(self, nums: List[int]) -> str:
        def quickSort(l, r):
            if l >= r:
                return None
            value = nums[r]
            i = l - 1
            for j in range(l, r):
                if nums[j] + value < value + nums[j]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[r] = nums[r], nums[i]
            quickSort(l, i-1)
            quickSort(i+1, r)

        nums = [str(x) for x in nums]
        quickSort(0, len(nums)-1)
        return ''.join(nums)