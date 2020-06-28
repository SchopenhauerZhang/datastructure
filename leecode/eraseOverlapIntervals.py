class Solution:
    def eraseOverlapIntervals(self, intervals: list) -> int:
        """
        给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

        注意:

        可以认为区间的终点总是大于它的起点。
        区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
        示例 1:

        输入: [ [1,2], [2,3], [3,4], [1,3] ]

        输出: 1

        解释: 移除 [1,3] 后，剩下的区间没有重叠。
        示例 2:

        输入: [ [1,2], [1,2], [1,2] ]

        输出: 2

        解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
        示例 3:

        输入: [ [1,2], [2,3] ]

        输出: 0

        解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/non-overlapping-intervals
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _eraseOverlapIntervals(self, intervals: list) -> int:
        if len(intervals) <= 1:
            return 0
        if len(intervals) == 2:
            return 1 if intervals[0][1] >intervals[1][0]  else 0 

        intervals_sorted = sorted(intervals,key=lambda x:x[1])
        sign = 0 
        interval_start = intervals_sorted.pop(0)
        for interval in intervals_sorted:
            if interval[0] < interval_start[1]:
                sign += 1
            else:
                interval_start = interval

        return sign
#print(Solution()._eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))
#print(Solution()._eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))

    def _eraseOverlapIntervals_eg(self, intervals: list) -> int:
        intervals.sort(key=lambda x:x[0])
        most_r = float('-inf')
        res = 0
        for i in range(len(intervals)):
            l, r = intervals[i]
            if l < most_r:
                res += 1
                if r < most_r:
                    most_r = r
            else:
                most_r = r
        return res