from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            现在你总共有 n 门课需要选，记为 0 到 n-1。

            在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

            给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

            可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

            示例 1:

            输入: 2, [[1,0]] 
            输出: [0,1]
            解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
            示例 2:

            输入: 4, [[1,0],[2,0],[3,1],[3,2]]
            输出: [0,1,2,3] or [0,2,1,3]
            解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
                 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
            说明:

            输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
            你可以假定输入的先决条件中没有重复的边。
            提示:

            这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
            通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
            拓扑排序也可以通过 BFS 完成。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/course-schedule-ii
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        def dfs(i):
            if flags[i] == 1: return False
            if flags[i] == -1: return True
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j): return False
            flags[i] = -1
            lst.append(i)
            return True
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        lst = []
        for cur,pre in prerequisites:
            adjacency[cur].append(pre)
        for i in range(numCourses):
            if not dfs(i): return []
        return lst
    
    def _findOrder_eg(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        result = list()
        # 判断有向图中是否有环
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    valid = False
                    return
            # 将节点标记为「已完成」
            visited[u] = 2
            # 将节点入栈
            result.append(u)
        
        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        if not valid:
            return list()
        
        # 如果没有环，那么就有拓扑排序
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]
