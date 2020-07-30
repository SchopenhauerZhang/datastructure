class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        if k == 0 or not nums or len(nums) == 1:
            return nums

        k = k if k < len(nums) else k % len(nums) 
        
        return  nums[len(nums)-k:]+nums[:len(nums)-k]
    
    def _rotate(self, nums: list, k: int) -> None:
        pass

# print(Solution().rotate([1,2,3,4,5,6,7],3))
# print(Solution().rotate([1,7],15))

    def search(self, arr: list, target: int) -> int:
        """
        搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

        示例1:

        输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
        输出: 8（元素5在该数组中的索引）
        示例2:

        输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
        输出：-1 （没有找到）

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/search-rotate-array-lcci
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not arr or target not in arr:
            return -1

        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

# print(Solution().search([1,2,3,4,5,6,7],3))
# print(Solution().search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],5))

    def _search_eg(self, arr: list, target: int) -> int:
        '''
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

        [16,17,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        不管反转几下，实际是只反转了一下

        假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

        [2,2,2,2,2,2,2,5,6,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        '''
        if not arr: return -1
        left, right = 0, len(arr) - 1
        flag = 0
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[right]:
                if arr[mid] < target < arr[right]:
                    left = mid + 1
                elif arr[mid] == target:
                    right = mid
                elif arr[right] == target:
                    flag = 1
                    res = right
                    right = right - 1
                else:
                    right = mid - 1
            elif arr[mid] > arr[right]:
                if arr[mid] >= target >= arr[left]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target == arr[mid]:
                    right = mid
                else:
                    right = right - 1
        res = res if flag else -1
        return left if arr[left] == target else res

    def _search_sort(self, arr: list, target: int) -> int:
        
        if target not in arr or not arr or len(arr) in  (1,2):
            if target not in arr or not arr:
                return -1
            return 1 if len(arr) == 2 and arr[1] == target else 0

        l ,r = 0,len(arr)-1

        while l < r:
            mid = (l+r)//2
            if arr[mid] == target or arr[l] == target or arr[r] == target:
                if arr[l] == target or arr[r] == target:
                    return l if arr[l] == target else r

                return mid 
            elif arr[mid] < arr[r]:
                if arr[mid] < target < arr[r]:
                    l = mid+1
                elif arr[mid] > target:
                    r = mid -1
                elif target > arr[r]:
                    r = mid -1
            elif arr[mid] > arr[r]:
                if arr[mid] > target > arr[r]:
                    r = mid -1
                elif arr[mid] < target:
                    l = mid + 1

        return -1

print(Solution()._search_sort([1,2,3,4,5,6,7],3))