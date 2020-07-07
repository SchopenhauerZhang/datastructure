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


