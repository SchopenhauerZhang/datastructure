from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            给定一个二维网格和一个单词，找出该单词是否存在于网格中。

                单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

                 

                示例:

                board =
                [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
                ]

                给定 word = "ABCCED", 返回 true
                给定 word = "SEE", 返回 true
                给定 word = "ABCB", 返回 false
                 

                提示：

                board 和 word 中只包含大写和小写英文字母。
                1 <= board.length <= 200
                1 <= board[i].length <= 200
                1 <= word.length <= 10^3

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/word-search
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        row = len(board)
        col = len(board[0])

        def helper(i, j, k, visited):
            #print(i,j, k,visited)
            if k == len(word):
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                # y横轴
                # x纵轴
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited \
                and board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if helper(tmp_i, tmp_j, k+1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j)) # 回溯
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1,{(i, j)}) :
                        return True
        return False
        
    # def __init__(self):
    #     self.res = []

    # def exist(self, board, word):
    #     if not board: return False
    #     row, col = len(board), len(board[0])
    #     direction = {(1, 0), (0, 1), (-1, 0), (0, -1)}
    #     L = len(word) - 1
    
    #     def dfs(x, y, idx):
    #         self.res.append((x, y))
    #         if idx == L:
    #             return True
    #         idx += 1
    #         for r, c in direction:
    #             cur_r, cur_c = x + r, y + c
    #             if -1 < cur_r and cur_r < row and -1 < cur_c and cur_c < col and board[cur_r][cur_c] == word[idx] and (cur_r, cur_c) not in self.res:
    #                 t = board[cur_r][cur_c]
    #                 if dfs(cur_r, cur_c, idx):
    #                     return True
    #                 else:
    #                     self.res.pop()
    #         return False
            
    #     for i in range(row):
    #         for j in range(col):
    #             if board[i][j] == word[0]:
    #                 self.res = []
    #                 if dfs(i, j, 0):
    #                     return True
    #     return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n, lw = len(board), len(board[0]), len(word)

        def dfs(word, cur, i, j):
            tmp = board[i][j]
            board[i][j] = 0
            cur += 1
            if cur == lw: return True
            if i > 0 and board[i-1][j] == word[cur]:
                if dfs(word, cur, i-1, j): return True

            if j > 0 and board[i][j-1] == word[cur]:
                if dfs(word, cur, i, j-1): return True
            
            if i < m-1 and board[i+1][j] == word[cur]:
                if dfs(word, cur, i+1, j): return True
            
            if j < n-1 and board[i][j+1] == word[cur]:
                if dfs(word, cur, i, j+1): return True
            
            board[i][j] = tmp
            return False
        
        need = {}
        for c in word:
            if c not in need: need[c] = 1
            else: need[c] += 1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in need: need[board[i][j]] -= 1
        
        if any(map(lambda x: x > 0, need.values())): return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    cur = 0
                    if dfs(word, cur, i, j): return True
        
        return False