class Solution:
    def removeDuplicates(self, nums: list) -> int:
        """
        给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

        不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

        示例 1:

        给定数组 nums = [1,1,2], 

        函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

        你不需要考虑数组中超出新长度后面的元素。
        """
        pass

    def _removeDuplicates(self, nums: list) -> int:
        #快慢指针
        if len(nums) <=1:
            return len(nums)
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return len(nums)
            nums.pop()
            return len(nums)
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1 
        for i in range(slow+1,len(nums)):
            nums.pop()
        
        return len(nums)    
#print(Solution()._removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

    def _removeDuplicates_better(self, parameter_list):
        index = 0
        for i in range(1,len(nums)):
            if nums[i]  != nums[index]:
                index +=1
                nums[index] = nums[i]
        return index+1 if nums else 0
        
    def _removeDuplicates_link_list(self,link_list):
        head = link_list
        slow = fast = head
        fast = head.next
        while fast:
            if slow.val!=fast.val:
                slow.next=fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head

    def _removeDuplicates_80(self, nums: List[int]) -> int:
        """
            给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

            不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

            示例 1:

            给定 nums = [1,1,1,2,2,3],

            函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

            你不需要考虑数组中超出新长度后面的元素。
            示例 2:

            给定 nums = [0,0,1,1,1,1,2,3,3],

            函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

            你不需要考虑数组中超出新长度后面的元素。
            说明:

            为什么返回数值是整数，但输出的答案是数组呢?

            请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

            你可以想象内部操作如下:

            // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
            int len = removeDuplicates(nums);

            // 在函数里修改输入数组对于调用者是可见的。
            // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
            for (int i = 0; i < len; i++) {
                print(nums[i]);
            }

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not nums or len(nums) <= 2:
            return 0 if not nums else len(nums)
        count = 1
        i,ll = 1,len(nums)
        while i < ll:
            if nums[i] == nums[i-1]:
                count -= 1
                if count < 0 :
                    del nums[i]
                    ll -= 1
                else:
                    i += 1
            else:
                count = 1
                i += 1
        return len(nums)
    
    def _removeDuplicates_80_eg(self, nums: List[int]) -> int:
        #counter = 1
        if len(nums) <= 2:
            return len(nums)
        i = 2
        while i<len(nums):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                del nums[i]
            else:
                i += 1
        return i
