# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
            给定一棵二叉搜索树，请找出其中第k大的节点。

         

        示例 1:

        输入: root = [3,1,4,null,2], k = 1
        3
        / \
        1   4
        \
           2
        输出: 4
        示例 2:

        输入: root = [5,3,6,2,4,null,null,1], k = 3
            5
            / \
            3   6
            / \
        2   4
        /
        1
        输出: 4

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return None
        node = self.kthLargest(root.right,k)
        if node:
            return node
        self.count += 1
        if self.count == k:
            return root
        node = self.kthLargest(root.left,k)
        if node:
            return node
        
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k, self.target = k, 0
        self.dfs(root)

        return self.target

    def dfs(self, root: TreeNode) -> None:
        if not root:
            return
        self.dfs(root.right)
        if self.k == 0:
            return
        self.k -= 1
        if self.k == 0:
            self.target = root.val
        self.dfs(root.left)

        return
        

