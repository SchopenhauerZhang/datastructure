

class Solution:
    def minDistance(self,word1,word2):
        """
        你可以对一个单词进行如下三种操作：

        插入一个字符
        删除一个字符
        替换一个字符
         

        示例 1：

        输入：word1 = "horse", word2 = "ros"
        输出：3
        解释：
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')
        """
        i = len(word1)
        j = len(word2)
        mem = dict()
        def dp(i,j):
            if (i,j) in mem:
                return mem[(i,j)] 

            if word1[i] == word2[j]:
                mem[(i,j)] = dp(i-1,j-1)
                return mem[(i,j)]
            else:
                mem[(i,j)] =  min(
                    dp(i-1,j)+1,
                    dp(i,j-1)+1,
                    dp(i-1,j-1)+1
                )
                return mem[(i,j)]
        
        return dp(i-1,j-1)

#print(Solution().minDistance("abcde","ace"))
    def _minDistance(self,word1,word2):
        from collections import deque
        visit, dq = set(), deque([(word1, word2, 0)])
        while True:
            w1, w2, d = dq.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2 = w1[1:], w2[1:]
                d += 1
                dq.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d),
                           (w1[1:], w2, d)])

print(Solution()._minDistance("abcde","ace"))


