from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        from collections import defaultdict
        orders = defaultdict(int)
        for i,j in enumerate(order):
            orders[j] = i
        tmp = []
        for i in ''.join(words):
            for j in range(len(tmp)):
                if orders[i] > tmp[j]:
                    return False
                elif orders[i] == tmp[j]:
                    break
            if orders[i] not in tmp:
                tmp.append(orders[i])
        return True

            
