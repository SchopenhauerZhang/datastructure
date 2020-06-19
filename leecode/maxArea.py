class Solution:
    def maxArea(self, height: list) -> int:
        """
        给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

        说明：你不能倾斜容器，且 n 的值至少为 2。
        输入：[1,8,6,2,5,4,8,3,7]
        输出：49
        """
        pass

    def _maxArea(self, height: list) -> int:
        if len(height) <= 2:
            return 0
        if len(height) == 3:
            return max(height[0] ,height[2])- height[1] if max(height[0] ,height[2])- height[1] > 0 else 0

        left = 0
        right = len(height)-1
        sum_p = 0
        l_max = height[left]
        r_max = height[right]
        left = 1
        right -= 1

        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                sum_p += l_max - height[left]
                left += 1
            else:
                sum_p += r_max - height[right]
                right -= 1

        return sum_p
#print(Solution()._maxArea([1,8,6,2,5,4,8,3,7]))

    def _maxArea_(self, height: list) -> int:
        # if len(height) <= 2:
        #     return 0
        # if len(height) == 3:
        #     return max(height[0] ,height[2])- height[1] if max(height[0] ,height[2])- height[1] > 0 else 0

        left = 0
        right = len(height)-1
        sum_p = 0
        l_max = height[left]
        r_max = height[right]
 

        while left < right:
            #l_max = max(l_max, height[left])
            #r_max = max(r_max, height[right])
            b = right - left
            if height[left] < height[right]:
                #sum_p += l_max - height[left]
                h = height[left]
                left += 1
                
            else:
                #sum_p += r_max - height[right]
                h = height[right]
                right -= 1
                
            if b*h > sum_p:
                sum_p = b*h 

        return sum_p
#print(Solution()._maxArea_([1,8,6,2,5,4,8,3,7]))

    def _maxArea_eg(self, height: list) -> int:
        n = len(height)
        max_area = 0

        start = 0 
        end = n-1
        for i in range(n):
            if end > start:
                if height[end] > height[start]:
                    area = (end-start)*height[start]
                    start += 1
                else:
                    area = (end-start)*height[end]
                    end -= 1

            if area > max_area:
                max_area = area 
        



        # for i in range(n):
        #     for j in range(n-1,i,-1):
        #         if max_height > height[j]:
        #             continue
        #         area = (j-i)*min(height[i],height[j])
        #         if area > max_area:
        #             max_area = area
        #             max_height = height[j]
        
        return max_area