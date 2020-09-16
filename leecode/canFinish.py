from typing import List
class Solution:
    def canFinish(self, N, prerequisites):
        """
            你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

            在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

            给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

             

            示例 1:

            输入: 2, [[1,0]] 
            输出: true
            解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
            示例 2:

            输入: 2, [[1,0],[0,1]]
            输出: false
            解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
             

            提示：

            输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
            你可以假定输入的先决条件中没有重复的边。
            1 <= numCourses <= 10^5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/course-schedule
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    #一定有一门课是不需要前提条件就能学的
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegrees[j] = -1
            for node in graph[j]:
                # 这门课的后修课程清空
                indegrees[node] -= 1
        return True 
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1. 课程表必须是一个【有向无环图】
        2. 通过【深度优先遍历】判断图中是否有环
        3. 输入的先决条件是由【边缘列表】表示的图形，而不是【邻接矩阵】 。
        """
        def recur(i, adjacency, flags):
            """递归验证课程i的是否完成"""
            if flags[i] == -1:  #点被其它节点启动的dfs访问过
                return True
            if flags[i] == 1:  #点被当前节点启动的dfs访问过，即存在闭环
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not recur(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True


        adjacency = [[] for _ in range(numCourses)]  #用于存储各门课程的先修课程
        flags = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites: # 存储每一门课的先修课程
            adjacency[cur].append(pre)
        
        # 对于每一门课程，递归验证其先决条件的先决条件的...是否包含自己，即闭环
        for i in range(numCourses):
            if not recur(i, adjacency, flags):
                return False
        return True
