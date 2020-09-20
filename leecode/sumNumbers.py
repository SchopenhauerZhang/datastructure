# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
            给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

            例如，从根到叶子节点路径 1->2->3 代表数字 123。

            计算从根到叶子节点生成的所有数字之和。

            说明: 叶子节点是指没有子节点的节点。

            示例 1:

            输入: [1,2,3]
                1
            / \
            2   3
            输出: 25
            解释:
            从根到叶子节点路径 1->2 代表数字 12.
            从根到叶子节点路径 1->3 代表数字 13.
            因此，数字总和 = 12 + 13 = 25.
            示例 2:

            输入: [4,9,0,5,1]
                4
            / \
            9   0
             / \
            5   1
            输出: 1026
            解释:
            从根到叶子节点路径 4->9->5 代表数字 495.
            从根到叶子节点路径 4->9->1 代表数字 491.
            从根到叶子节点路径 4->0 代表数字 40.
            因此，数字总和 = 495 + 491 + 40 = 1026.

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return 0
        res = []
        def tree(rt,_res):
            if not rt:
                return res.append(_res)
            if not rt.left and not rt.right:
                return res.append(_res+str(rt.val))
            if not rt.right:
                tree(rt.left,_res+str(rt.val))
            elif not rt.left:
                tree(rt.right,_res+str(rt.val))
            else:
                tree(rt.left,_res+str(rt.val))
                tree(rt.right,_res+str(rt.val))
            return 
        tree(root,'')
        print(res)
        return sum([int(i) for i in res])

    def sumNumbers_eg(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, root.val))
        res = 0
        while len(queue) > 0:
            node, curr_val = queue.popleft()
            if node.left:
                # 继续BFS
                queue.append((node.left, curr_val * 10 + node.left.val))
            if node.right:
                # 继续BFS
                queue.append((node.right, curr_val * 10 + node.right.val))
            if not node.left and not node.right:
                # 找到了一个leaf node，累计结果
                res += curr_val
        return res