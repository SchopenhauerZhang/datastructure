from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not numCourses or  numCourses <= 2 or len(prerequisites) == 1:
            if numCourses == 1 and len(prerequisites) == 1:
                return True if prerequisites[0][0] != prerequisites[0][1] else False
            return True if numCourses == 2 and  len(prerequisites) == 1 and prerequisites[0][0] != prerequisites[0][1] else False
        temp = []
        for l,r in prerequisites:
            if l != r:
                if l not in temp and r not in temp :
                    temp.append(l)
                    if len(temp) == numCourses:
                        return True
            else:
                return False
        if prerequisites[-1][1] not in temp:
            temp.append(prerequisites[-1][1])
        return False if len(temp) < numCourses else True