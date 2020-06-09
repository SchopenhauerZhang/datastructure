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