class Solution:
    def merge(self, intervals: list) -> list:
        """
        给出一个区间的集合，请合并所有重叠的区间。

        示例 1:

        输入: [[1,3],[2,6],[8,10],[15,18]]
        输出: [[1,6],[8,10],[15,18]]
        解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
        示例 2:

        输入: [[1,4],[4,5]]
        输出: [[1,5]]
        解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/merge-intervals
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _merge(self, intervals: list) -> list:
        if len(intervals)<=1:
            return intervals
        interval = sorted(intervals) 
        #if len(intervals) ==2:
        #    return [[intervals[0][0],intervals[1][1]]] if intervals[0][1]>= intervals[1][0] else intervals
        start ,end = intervals[0]
        res = []

        for i in interval:
            if min(i) <= max(start,end): 
                start = min(start,i[0])
                end = max(end,i[1])
            else:
                res.append([start,end])
                start = i[0]
                end = i[1]
        res.append([start,end])
        return res
# print(Solution()._merge([[1,4],[0,0]]))
# print(Solution()._merge([[1,4],[0,4]]))
# print(Solution()._merge([[1,4],[4,5]]))
# print(Solution()._merge([[1,3],[2,6],[8,10],[15,18]]))

    def _merge_(self,intervals):
        if not intervals: return []
        # 按区间的 start 升序排列
        intervals.sort(key=lambda intv: intv[0])
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            curr = intervals[i]
            # res 中最后一个元素的引用
            last = res[-1]
            if curr[0] <= last[1]:
                # 找到最大的 end
                last[1] = max(last[1], curr[1])
            else:
                # 处理下一个待合并区间
                res.append(curr)
        return res

    def _merge_(self,intervals):
        if not intervals:
            return []
        intervals.sort(key = lambda a:a[0])
        ans = []
        begin = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] > end:
                ans.append([begin,end])
                begin = interval[0]
                end = interval[1]
            else:
                end = max(end, interval[1])
        ans.append([begin, end])
        return ans
