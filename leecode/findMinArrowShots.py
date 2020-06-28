class Solution:
    def findMinArrowShots(self, points: list) -> int:
        """
        在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。

        一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

        Example:

        输入:
        [[10,16], [2,8], [1,6], [7,12]]

        输出:
        2

        解释:
        对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _findMinArrowShots(self, points: list) -> int:
        arrow = 0
        if not points:
            arrow = 0
        if len(points) == 1 or (len(points) == 2 and points[0][1] >= points[1][0] ):
            arrow = 1
        elif len(points) == 2:
            arrow = 2

        if len(points) >= 3:
            points.sort(key=lambda x : x[0])
            l,arrow_p = points.pop(0)
            arrow += 1
            
            for i in range(len(points)):
                if arrow_p < points[i][0]:
                    
                    arrow += 1
                    arrow_p = points[i][1]
                else:
                    if arrow_p > points[i][1]:
                        arrow_p = points[i][1]

        return arrow
#print(Solution()._findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
#print(Solution()._findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))

    def _findMinArrowShots_eg(self, points: list) -> int:
        if not points: return 0
        N = len(points)
        points.sort(key=lambda x: x[1])
        _, cur_end = points.pop(0)
        res = 1
        for start, end in points:
            if start > cur_end:
                res += 1
                cur_end = end
        return res

