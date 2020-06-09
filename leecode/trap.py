class Solution:
    def trap(self, s: list) -> str:
        """
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
        示例:
        输入: [0,1,0,2,1,0,1,3,2,1,2,1]
        输出: 6
        """
        pass

    def _trap_for(self, s: list) -> str:
        container = 0

        for i in range(1,len(s)):
            l_max = r_max = 0
            for l in range(i):
                l_max = max(s[l],l_max)
            for r in range(i+1,len(s)):
                r_max = max(s[r],r_max)
            
            container += min(l_max,r_max)-s[i] if min(l_max,r_max)-s[i] > 0  else 0

        return container
#print(Solution()._trap_for([0,1,0,2,1,0,1,3,2,1,2,1]))

    def _trap_container(self, s: list) -> str:
        if len(s)<=2:
            return 0
        container = 0
        import copy
        r_max = [0]*len(s)
        l_max = copy.deepcopy(r_max)
        l_max[0] = s[0]
        
        for l in range(1,len(s)):
            l_max[l] = max(s[l],l_max[l-1])

        r_max[len(s)-1] = s[len(s)-1]
        for r in range(len(s)-2,0,-1):
            r_max[r] = max(s[r],r_max[r+1])

        for i in range(1,len(s)):
            container += min(l_max[i],r_max[i])-s[i] if min(l_max[i],r_max[i])-s[i] > 0  else 0

        return container
#print(Solution()._trap_container([2,0,2]))

    def _trap_pointer(self, height: list) -> str:
        s = height
        if len(s)<=2:
            return 0
        container = 0
        l_max = s[0]
        r_max = s[len(s)-1]
        right = len(s)-2
        left = 1
        while left <= right:
            l_max = max(l_max,s[left])
            r_max = max(r_max,s[right])
            if l_max < r_max:
                container += l_max-s[left]
                left += 1
            else:
                container += r_max-s[right]
                right -= 1

        return container
#print(Solution()._trap_pointer([2,0,2]))

    def _trap_better_eg(self, height: list) -> int:
        result = 0 # 最终返回的结果值
        left = 0 
        right = len(height) - 1
        left_max = 0
        right_max = len(height) - 1

        while left < right: # 控制边界
            if height[left] > height[right]: # 左边比右边高
                if height[right_max] < height[right]:
                    right_max = right
                    right -= 1
                else:
                    result += height[right_max] - height[right]
                    right -= 1
            
            if height[left] <= height[right]: # 左边不高于右边
                if height[left_max] < height[left]:
                    left_max = left
                    left += 1
                else:
                    result += height[left_max] - height[left]
                    left += 1

        return result

print(Solution()._trap_better_eg([2,0,2]))