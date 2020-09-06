from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
            假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

            注意：
            总人数少于1100人。

            示例

            输入:
            [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

            输出:
            [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not people:
            return []
        # 根据k排序
        people.sort(key=lambda x:x[1] , reverse = True)
        # 根据身高排序
        people.sort(key=lambda x:x[0] )
        res = []
        for i in range(len(people)-1,-1,-1):
            if not res:
                res.append(people[i])
            else:
                res.insert(people[i][1],people[i])
        return res
    
    def _reconstructQueue_eg(self, people: List[List[int]]) -> List[List[int]]:
        """
            精彩
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
        