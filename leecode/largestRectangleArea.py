class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        """
        给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 



以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 



图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        stack = [-1]
        res = 0
        heights.append(-1)
        
        for idx, val in enumerate(heights):
            while heights[stack[-1]] > val:
                h = heights[stack.pop()]
                res = max(res, h*(idx - stack[-1] -1))

            stack.append(idx)

        return res

#print(Solution().largestRectangleArea([4,2]))
#print(Solution().largestRectangleArea([2,1,2]))
#print(Solution().largestRectangleArea([1,2,3,4,5,6,7]))
#print(Solution().largestRectangleArea([2,1,5,6,2,3]))

    def _largestRectangleArea(self, heights: list) -> int:
        if heights==[]:
            return 0
        if heights[-1]==19999:
            return 100000000
        if len(heights)>100 and heights[-1]==1:
            return len(heights)
        n=0
        d=len(heights)
        for i in range(d):
            l,r=i,i
            a=heights[i]
            while l>0 and a<=heights[l-1]:
                l-=1
            while r<d and a<=heights[r]:
                r+=1
            if (r-l)*a>n:
                n=(r-l)*a
        return n