from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or (len(M)== 1 and len(M[0]) == 1):
            return 0 if not M or M[0][0] == 0 else 1 
        self.dp = []
        self.res = 0
        def find(_i,_j):
            if _i >=_c or _j >=_r:
                return 
            if M[_i][_j] == 1 and [i,j] not in self.dp:
                self.dp.append([i,j])
            elif M[_i][_j] != 1:
                return 
            M[i][j] = -1
            find(_i,_j+1)
            find(_i+1,_j)
            M[i][j] = 1
          
            return 
        _c,_r = len(M),len(M[0])
        for i in range(_c):
            for j in range(_r):
                if [i,j] in self.dp or M[i][j]!= 1:
                    continue
                print(self.dp)
                self.dp.append([i,j])
                find(i,j)
                self.res+= 1
                
        return self.res