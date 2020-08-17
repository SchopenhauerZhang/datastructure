from typing import List
class Solution():
    def __init__(self):
        super().__init__()
    
    # O(n) < O(n^2) < O(n^2) 
    def insert_sort(self,arr:list)->list:
        if len(arr) <= 2:
            return [arr[1],arr[0]] if len(arr) == 2 and arr[0] >arr[1] else arr
        for i in range(1,len(arr)):
            j = i -1
            key = arr[i]
            while j>= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def choice_sort(self,num:list)->list:
        if len(num) <= 2:
            return num[::-1]  if len(num) == 2 and num[0] > num[1] else num
        nums = []
        while num:
            _min = min(num)
            nums.append(_min)
            del num[num.index(_min)]
        return nums

    def quick_sort(self,num:list):
        if len(num) <= 2:
            return num[::-1] if len(num) == 2 and num[0] > num[1] else num
        cur,l,r = num[0],[],[]
        for _da in num[1:]:
            if _da < cur:
                l.append(_da)
            else:
                r.append(_da)
        return self.quick_sort(l)+[cur]+self.quick_sort(r)



