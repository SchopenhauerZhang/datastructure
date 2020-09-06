class Solution:
    
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

#print(Solution()._search_sort([1,2,3,4,5,6,7],3))

    def rotate(self, nums: list, k: int) -> None:
        """
        给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

        示例 1:

        输入: [1,2,3,4,5,6,7] 和 k = 3
        输出: [5,6,7,1,2,3,4]
        解释:
        向右旋转 1 步: [7,1,2,3,4,5,6]
        向右旋转 2 步: [6,7,1,2,3,4,5]
        向右旋转 3 步: [5,6,7,1,2,3,4]
        示例 2:

        输入: [-1,-100,3,99] 和 k = 2
        输出: [3,99,-1,-100]
        解释: 
        向右旋转 1 步: [99,-1,-100,3]
        向右旋转 2 步: [3,99,-1,-100]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/rotate-array
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        Do not return anything, modify nums in-place instead.
        """ 
       
        num = nums
        k = k if k < len(num) else k % len(num) 
        
        n = num[len(num)-k:]+num[:len(num)-k]
        for i in range(len(nums)):
            nums[i] = n[i]
    
    def _rotate_eg(self, nums: list, k: int) -> None:
        lenth = len(nums)
        nums[:] = nums[lenth-k:]+nums[:lenth-k]

#print(Solution().rotate([1,2,3,4,5,6,7],3))

    def _rotate_eg_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            while i < j:
                nums[i], nums[j] = nums[j] ,nums[i]
                i += 1
                j -= 1
        
        n = len(nums) - 1
        k %= n + 1
        swap(0, n)
        swap(0, k - 1)
        swap(k, n)

    '''
#方案一，删除后添加
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)        
        return 
'''

    #方案二，依次翻转，首先翻转前n-k个数，再翻转后k个数，最后翻转整个数组
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def _rotate_eg_2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        reverse(nums, 0, n-k-1)
        reverse(nums, n-k, n-1)
        nums.reverse()
        return
    
    def _rotate_48(self, matrix: List[List[int]]) -> None:
        """
            给定一个 n × n 的二维矩阵表示一个图像。

            将图像顺时针旋转 90 度。

            说明：

            你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

            示例 1:

            给定 matrix = 
            [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ],

            原地旋转输入矩阵，使其变为:
            [
            [7,4,1],
            [8,5,2],
            [9,6,3]
            ]
            示例 2:

            给定 matrix =
            [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
            ], 

            原地旋转输入矩阵，使其变为:
            [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
            ]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/rotate-image
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        Do not return anything, modify matrix in-place instead.
        
        """
        
        if len(matrix[0]) > 1:
            pass
        matrix[:] = zip(*matrix[::-1])
    
    def _rotate_48_eg(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cur_row = 0
        n = len(matrix[0])
        # leng = n - 1

        while cur_row < n:
            for indx1 in range(cur_row, (n-1)):
                # cur_col = indx1
                cur_pixel = matrix[cur_row][indx1]
                for _ in [0,1,2,3]:
                    new_row = indx1
                    # new_col = leng - cur_row
                    new_col = len(matrix[0]) - 1 - cur_row
                    next_pixel = matrix[new_row][new_col]
                    matrix[new_row][new_col] = cur_pixel
                    
                    cur_pixel = next_pixel
                    cur_row = new_row
                    indx1 = new_col
            
            cur_row += 1
            n -= 1