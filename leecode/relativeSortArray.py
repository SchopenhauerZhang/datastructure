from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
            给你两个数组，arr1 和 arr2，

            arr2 中的元素各不相同
            arr2 中的每个元素都出现在 arr1 中
            对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

             

            示例：

            输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
            输出：[2,2,2,1,4,3,3,9,6,7,19]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/relative-sort-array
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not arr1 or not arr2:
            return arr1 if arr1 else None
        from collections import Counter
        l = len(arr1)
        tmp = []
        _i =0 
        for _ in range(l):
            if arr1[_i] not in arr2:
                tmp.append(arr1[_i])
                del arr1[_i]
            else:
                _i += 1
        
        tmp.sort()

        a1 = Counter(arr1)
        index = 0
        for _ar in arr2:
            while a1[_ar] > 0:
                arr1[index] = _ar
                a1[_ar] -= 1
                index += 1


        return arr1 + tmp
#print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
#print(Solution().relativeSortArray([26,21,11,20,50,34,1,18],[21,11,26,20]))

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]
        ans = []
        for i in range(len(arr1)):
            arr[arr1[i]] += 1
        for i in range(len(arr2)):
            while arr[arr2[i]] > 0:
                ans.append(arr2[i])
                arr[arr2[i]] -= 1
        for i in range(len(arr)):
            while arr[i] > 0:
                ans.append(i)
                arr[i] -= 1
        return ans
        
          




