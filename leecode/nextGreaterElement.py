class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        """
        给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

            nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

            示例 1:

            输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
            输出: [-1,3,-1]
            解释:
                对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
                对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
                对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
            示例 2:

            输入: nums1 = [2,4], nums2 = [1,2,3,4].
            输出: [3,-1]
            解释:
                对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
                对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/next-greater-element-i
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _nextGreaterElement(self, nums1: list, nums2: list) -> list:
        import copy
        num = copy.deepcopy(nums2)
        nums = nums2
        # 非循环搜索
        if len(nums) <= 1:
            return nums
        if len(nums) <= 2:
            return  [nums[1],-1] if nums[0] < nums[1] else [-1,nums[0]]
        l = len(nums)-1
        stack = list()
        res = list()
        for _ in range(l+1):
            res.append(-1)

        while nums:
            _data = nums.pop()
            while stack and stack[len(stack)-1] <= _data:
                stack.pop()
            #res.append(stack[len(stack)-1] if stack else -1)
            res[l] = stack[len(stack)-1] if stack else -1
            stack.append(_data)
            l -= 1
        
        res1 = list()
        for _ in range(len(nums1)):
            res1.append(-1)

        for k,v in enumerate(nums1):
            if v not in num:
                res1[k] = -1
            else:
                res1[k] = res[num.index(v)]
        
        return res1
#print(Solution()._nextGreaterElement([4,1,2],[1,3,4,2]))

    def _nextGreaterElement_eg(self, nums1: list, nums2: list) -> list:
        stack, dic = [], dict()
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                dic[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        return [dic.get(num, -1) for num in nums1]


