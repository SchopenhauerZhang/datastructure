# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
            从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

         

        例如:
        给定二叉树: [3,9,20,null,null,15,7],

            3
        / \
        9  20
            /  \
        15   7
        返回其层次遍历结果：

        [
        [3],
        [9,20],
        [15,7]
        ]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return []
        stack = [[root]]
        res = []
        while stack:
            tmp = []
            _res =[ ]
            while stack :
                data = stack.pop()
                if data:
                    for _data in data:
                        res.append(_data.val)
                        if _data.left:
                            tmp.append(_data.left)
                        if _data.right:
                            tmp.append(_data.right)
            if _res:   
                res.append(_res)
            if tmp:
                stack.append(tmp)

        return res
            

    def _levelOrder_eg(self, root: TreeNode) -> List[List[int]]:
        self.res = []

        def func(queue):
            if not queue:
                return
            tem = []
            pre = []
            for cur in queue:
                tem.append(cur.val)
                if cur.left:
                    pre.append(cur.left)
                if cur.right:
                    pre.append(cur.right)
            self.res.append(tem)
            queue = pre
            func(queue)
        if not root:
            return self.res
        func([root])
        return self.res