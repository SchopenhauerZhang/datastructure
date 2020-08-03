# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

        二叉树的根是数组中的最大元素。
        左子树是通过数组中最大值左边部分构造出的最大二叉树。
        右子树是通过数组中最大值右边部分构造出的最大二叉树。
        通过给定的数组构建最大二叉树，并且输出这个树的根节点。

         

        示例 ：

        输入：[3,2,1,6,0,5]
        输出：返回下面这棵树的根节点：

            6
            /   \
        3     5
            \    / 
            2  0   
            \
                1
         

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/maximum-binary-tree
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        def BinaryTree(num,s,r):
            if not num:
                return None
    
            _max_i = s
            for _i in range(s,r+1,1):
                if num[_i] > num[_max_i]:
                    _max_i = _i
            print(_max_i)
            node = TreeNode(num[_max_i])
            if s < _max_i:
                node.left = BinaryTree(num,s,_max_i-1)
            if _max_i < r:
                node.left = BinaryTree(num,_max_i+1,r)

            return node

        return BinaryTree(nums,0,len(nums)-1)

    def _constructMaximumBinaryTree_eg(self, nums: List[int]) -> TreeNode:
        # O(n) stack
        stack = []
        n = len(nums)
        if n == 0: return None
        for num in nums:
            cur = TreeNode(num)
            # pop 
            while len(stack) > 1 and stack[-1].val < cur.val:
                stack[-1].right = stack.pop()
                
            if stack and stack[-1].val < cur.val:
                cur.left = stack.pop()
                
            elif stack and stack[-1].val > cur.val: 
                cur.left = stack[-1].right
                stack[-1].right = None
            
            stack.append(cur)
        # deal with stack
        while len(stack) > 1:
            stack[-1].right = stack.pop()
        return stack[0]