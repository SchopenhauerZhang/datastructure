from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
            给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

            如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

             

            示例 1：

            输入：arr = [1,2,2,1,1,3]
            输出：true
            解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
            示例 2：

            输入：arr = [1,2]
            输出：false
            示例 3：

            输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
            输出：true

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/unique-number-of-occurrences
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not arr or len(arr) <=2:
            return True if len (arr) == 1 or (len (arr) == 2 and arr[0] == arr[1])  else False
        from collections import Counter
        arr_c = Counter(arr)
        tmp = []
        for i in arr_c:
            if arr_c[i] not in tmp:
                tmp.append(arr_c[i])
            else:
                return False
        return True