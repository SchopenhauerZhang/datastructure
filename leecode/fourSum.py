from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            四数之和
            给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

            注意：

            答案中不可以包含重复的四元组。

            示例：

            给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

            满足要求的四元组集合为：
            [
            [-1,  0, 0, 1],
            [-2, -1, 1, 2],
            [-2,  0, 0, 2]
            ]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/4sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            超出时间限制
        """
        if not nums or target is None:
            return []
        nums.sort()
        print( nums)
        ll = len(nums)
        res = []
        for i in range(ll-3):
            if i>0 and nums[i] == nums[i-1]:
                    continue
          
            for j in range(i+1,ll-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+1,ll-1
                while l < r:
                    
                    
                    if nums[i]+nums[j]+nums[l]+nums[r] == target:
                        
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        
                        while l<r and nums[l] == nums[l+1]:
                            l += 1
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        l+=1
                        r-=1
                    elif nums[i]+nums[j]+nums[l]+nums[r] > target:
                        r -= 1
                    elif nums[i]+nums[j]+nums[l]+nums[r] < target:
                        l += 1
                    
        return res
                
    def _fourSum_eg(self, nums: List[int], target: int) -> List[List[int]]:
        counter={}
        for n in nums:
            counter[n]=counter.get(n,0)+1
        nums=sorted(counter)
        ans,N=[],len(nums)
        for i in range(N):
            a=nums[i]
            if a*4> target:
                break
            if a+3*nums[-1]<target:
                continue
            counter[a]-=1
            for j in range(i if counter[a]>0 else i+1,N):
                b=nums[j]
                if a+b*3>target:
                    break
                if a+b+nums[-1]*2<target:
                    continue
                counter[b]-=1
                for k in range(j if counter[b]>0 else j+1,N):
                    c=nums[k]
                    d=target-a-b-c
                    if c>d:
                        break
                    if d not in counter or c==d and counter[c]<2:
                        continue
                    ans.append([a,b,c,d])
                counter[b]+=1
        return ans
