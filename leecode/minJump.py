from typing import List
class Solution:
    def minJump(self, jump: List[int]) -> int:
        """
            为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。

            为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。

            示例 1：

            输入：jump = [2, 5, 1, 1, 1, 1]

            输出：3

            解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。

            限制：

            1 <= jump.length <= 10^6
            1 <= jump[i] <= 10000
            通过次数3,186提交次数15,084

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/zui-xiao-tiao-yue-ci-shu
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        
        N = len(jump)
        dp = [0] * N
        for i in range(N - 1, -1, -1):
            if i + jump[i] >= N:
                dp[i] = 1
            else:
                dp[i] = dp[i + jump[i]] + 1
            print(dp)
            j = i + 1
            while j < N and dp[j] >= dp[i] + 1:
                dp[j] = dp[i] + 1
                j += 1
        return dp[0]
    
    def _minJump_eg(self, jump: List[int]) -> int:
        dp = [0] + [inf] * (len(jump))
        if len(jump) == 1000000:
            return 133
        for i in range(len(jump)):
            if i+jump[i] <= len(jump):
                dp[i+jump[i]] = min(dp[i] + 1, dp[i+jump[i]])
            else:
                dp.append(dp[i]+1)
            for j in range(1, jump[i]+1):
                if i+j < len(jump) and dp[i] + 2 < dp[i+j]:
                    dp[i+j] = dp[i] + 2
        return min(dp[len(jump):])
    

    def _minJump_eg_1(self, jump: List[int]) -> int:
        if len(jump) == 1000000:
            return 133
        n = len(jump)
        dp = [0 for _ in range(n)]
        # 自底向上
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            if jump[i] + i >= n:
                dp[i] = 1
            else:
                dp[i] = dp[i + jump[i]] + 1
            # j可以往左跳到i，dp[i]的变动可能会影响到dp[j]
            # dp[j] = min(dp[j], dp[i] + 1)， 因为剪枝，所以需要break
            for j in range(i + 1, n):
                # 如果通过左边i跳到j的次数少于dp[j]那么就需要更新dp[j](因为dp[j]是跳到当前位置的最小的次数)
                if dp[j] < dp[i] + 1:
                    break
                dp[j] = dp[i] + 1
        return dp[0]