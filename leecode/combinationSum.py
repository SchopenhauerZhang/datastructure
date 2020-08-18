from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) <= 1 or not  target:
            return [[candidates[0]]*(target//candidates[0])] if candidates and target%candidates[0]==0 else []
        res = []
        def combination(can,tagt,_res):
            nonlocal res
            for i in range(len(can)):
                if tagt % can[i] == 0:
                    res.append(_res+[can[i]*(tagt // can[i])])
                else:
                    _tagt = _tagt % can[i]
                    _res = _res+[can[i]*(_tagt // can[i])]
                    combination(can[i+1:],_tagt,_res)
            
        combination(candidates,target,[])

        return res
