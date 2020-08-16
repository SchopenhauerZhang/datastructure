# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    res = []
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
    
    def _levelOrder_32(self, root: TreeNode) -> List[int]:
        """
            从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

             

            例如:
            给定二叉树: [3,9,20,null,null,15,7],

                3
            / \
            9  20
                /  \
            15   7
            返回：

            [3,9,20,15,7]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return []
        elif root and not root.left and not root.right:
            return [root.val]
        que = [[root]]
        while que:
            tmp = []
            while que:
                node = que.pop()
                _que = []
                for _node in node:
                    if _node:
                        tmp.append(_node.val)
                    if _node.left:
                        _que.append(_node.left)
                    if _node.right:
                        _que.append(_node.right)
            if tmp:
                self.res += tmp
            if _que:
                que.append(_que)
        return self.res

    def _levelOrder_32_eg(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:queue.append(node.left)
            if node.right:queue.append(node.right)
        return res
    
    def _levelOrder_III(self, root: TreeNode) -> List[List[int]]:
        """
            请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
            [20,9],
            [15,7]
            ]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not pRoot:
            return []
        queue = [pRoot]
        ans = []
        count = 0
        while queue:
            temp = []
            res = []
            count += 1
            for i in queue:
                res.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp
            if count%2 == 0:
                res = res[::-1]
            ans.append(res)
        return ans
    
    def _levelOrder_III_32_eg(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,dq = [],collections.deque()
        dq.append(root)
        while dq:
            tmp = collections.deque()
            for _ in range(len(dq)):
                node = dq.popleft()
                if len(res)%2:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(list(tmp))
        return res
    
    def _levelOrder_102(self, root: TreeNode) -> List[List[int]]:
        """
            给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

             

            示例：
            二叉树：[3,9,20,null,null,15,7],

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
            通过次数178,532

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        res = []
        if not root or (not root.left and not root.right): 
            return [] if not root else [[root.val]]
        q = [root]
        while q:
            _tmp = []
            _q = []
            for i in q:
                _tmp.append(i.val)
                if i.left:
                    _q.append(i.left)
                
                if i.right:
                    _q.append(i.right)
            if _q:
                q = _q
            else :
                q = []
            if _tmp:
                res.append(_tmp)
        return res
    
    def _levelOrder_102_eg(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res=[]
        cur_lev=[root]
        while cur_lev:
            nex_lev=[]
            tmp=[]
            for cur in cur_lev:
                tmp.append(cur.val)
                if cur.left:
                    nex_lev.append(cur.left)
                if cur.right:
                    nex_lev.append(cur.right)
            res.append(tmp)
            cur_lev=nex_lev
        return res