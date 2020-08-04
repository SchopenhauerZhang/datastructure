from typing import List
class Solution:
    def search(self, nums: list, target: int) -> int:
        if target not in nums:
            return -1

        l,r = 0,len(nums)-1
        
        while l < r:
            if nums[l] == target or nums[r] == target:
                return l if nums[l] == target else r
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1

        return l if nums[l] == target else -1
#print(Solution().search([-1,0,3,5,9,12],9))

    def _search_eg(self, nums: List[int], target: int) -> int:
        def fun(left, right, target):
            if left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return fun(left, mid - 1, target)
                else:
                    return fun(mid + 1, right, target)
            else:
                return -1
        return fun(0, len(nums) - 1, target)

    def _search_xuanzhuan(self, A, target: int) -> int:
        """
        假设按照升序排序的数组在预先未知的某个点上进行了旋转。

        ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

        搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

        你可以假设数组中不存在重复的元素。

        你的算法时间复杂度必须是 O(log n) 级别。

        示例 1:

        输入: nums = [4,5,6,7,0,1,2], target = 0
        输出: 4
        示例 2:

        输入: nums = [4,5,6,7,0,1,2], target = 3
        输出: -1

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
            # mid左端是排好序的
            if A[mid] >= A[left]:
                # 因为前面第11行的判断已经说明A[mid] != target了，所以不再考虑A[mid] = target的情况
                if A[mid] > target and A[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # 下面的else等同于elif A[mid] <= A[right]
            else:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# print(Solution()._search_xuanzhuan([4,5,6,7,0,1,2],0))

    def _search_xuanzhuan_eg(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1 
        
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2 
            #### 转点在左边 右边单调增
            if nums[mid] < nums[end]:
                if nums[mid] > target or nums[end] < target:
                    end = mid 
                else:
                    start = mid 
            
            else:
                if nums[mid] < target or nums[start] > target:
                    start = mid 
                else:
                    end = mid 
        
        if nums[start] == target:
            return start 
        if nums[end] == target:
            return end 
        return -1

