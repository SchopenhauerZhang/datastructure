from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
            n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
            上图为 8 皇后问题的一种解法。

            给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

            每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

             

            示例：

            输入：4
            输出：[
            [".Q..",  // 解法 1
            "...Q",
            "Q...",
            "..Q."],

            ["..Q.",  // 解法 2
            "Q...",
            "...Q",
            ".Q.."]
            ]
            解释: 4 皇后问题存在两个不同的解法。
             

            提示：

            皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/n-queens
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            n queens
        """
        # 无解
        if n < 4:
            return [['Q']] if n == 1 else []
        res = []
        row_res = '.'*n
        def nqueues(row,_res,col_set,sum_set,reduce_set):
            if row == n:
                # 退出条件是摆完所有行[列]
                res.append(_res)
                return 
            # 按行再按列遍历
            for _col in range(n):
                # 列不重复并且不在一条斜线上
                if _col not in col_set and row+_col not in sum_set and row-_col not in reduce_set:
                    nqueues(row+1,_res+[row_res[:_col]+'Q'+row_res[_col+1:]],col_set|{_col},sum_set|{_col+row},reduce_set|{row-_col})
        nqueues(0,[],set(),set(),set())
        return res

    def _solveNQueens_eg(self, n: int) -> List[List[str]]:
        def dfs(r):
            if r == n:
                all_rows = []
                for i in range(n):
                    row[queens[i]] = 'Q'
                    all_rows.append(''.join(row))
                    row[queens[i]] = '.'
                res.append(all_rows)
            else:
                for c in range(n):
                    if c in cols or r - c in dig1 or r + c in dig2:
                        continue
                    cols.add(c)
                    dig1.add(r - c)
                    dig2.add(r + c)
                    queens[r] = c
                    dfs(r + 1)
                    queens[r] = -1
                    cols.remove(c)
                    dig1.remove(r - c)
                    dig2.remove(r + c)

        res = []
        row = ['.'] * n
        queens = [-1] * n
        cols = set()
        dig1 = set()
        dig2 = set()
        dfs(0)
        return res
    