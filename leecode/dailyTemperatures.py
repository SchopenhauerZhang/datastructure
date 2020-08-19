from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
            请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

            例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

            提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/daily-temperatures
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not T or len(T) <= 2:
            if len(T) == 2:
                return [1,0] if T[0] < T[1] else [0,0]
            return [0] if T else []
        stack = []
        i = 0
        res = [0] *len(T)
        while i < len(T):
            if not stack:
                stack.append(i)
            else:
                while stack:
                    if T[stack[-1]] < T[i]:
                        x = stack.pop()
                        res[x]=i-x
                    else:
                        break
                stack.append(i)
            i += 1
        while stack:
            x = stack.pop()
            if x == len(T)-1:
                res[x]=0
            else:
                res[x]=0
        return res
    
    def _dailyTemperatures_eg(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0] * n
        stack = []
        for i in range(0,n):
            while stack and T[i] > T[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans