# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

         

        例如，给出

        前序遍历 preorder = [3,9,20,15,7]
        中序遍历 inorder = [9,3,15,20,7]
        返回如下的二叉树：

            3
        / \
        9  20
            /  \
        15   7

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not preorder or not inorder:
            return None
        elif len(preorder) ==1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            # 先序遍历第一个是head.left,# 中序遍历head的左边都是left
            in_i = inorder.index(preorder[0])
            in_l = inorder.index(preorder[0])+1# left为中序遍历的左子树的最后一个节点
            root.left = self.buildTree(preorder[1:in_l+1],inorder[:in_i])
            # 先序遍历的第二个开始是right,# 中序遍历的右边是right
            in_r = inorder.index(preorder[0])+1# right为中序遍历的右子树的最后一个节点
            root.right = self.buildTree(preorder[in_r:],inorder[in_i+1:])
            return root

    def _buildTree(self, pre, tin):
        lon = len(pre)
        if lon == 0:
            return None
        elif lon == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            #这一步看似稍微写的有点复杂，但其实只是省了一些中间变量，pre[0]是读取的根节点，tin.index将根节点定位，那么根节点的左子树从1开始，到tin.index+1结束，建议自己在纸上将这部分框出来，就好理解的多了。
            root.left = self.buildTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
            root.right = self.buildTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
            return root

    def _buildTree_eg(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        table = {}
        for i in range(len(inorder)):
            table[inorder[i]] = i ## inorder index 
        def recur(pre_idx, L, R):
            if L > R: return None 
            val = preorder[pre_idx]
            root = TreeNode(val)
            ino_idx = table[val]
            root.left = recur(pre_idx+1, L, ino_idx-1)
            root.right = recur(pre_idx+ (ino_idx-L) + 1, ino_idx+1, R)
            return root 
        return recur(0, 0, len(inorder)-1)
    
    def _buildTree_105(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or  not inorder or len(preorder) == 1:
            return TreeNode(preorder[0])  if preorder else None
        
        def build(prepos,l,r):
            root = TreeNode(preorder[prepos])
            # 左右子树定位
            right = inorder.index(preorder[prepos])

            root.left = build(prepos+1,l,right-1)
            root.right = build(prepos+right-l+1,right+1,r)
        
        return build(0,0,len(preorder)-1)
    
    def _buildTree_105_eg(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def createTree(preorder_left,preorder_right,inorder_left,inorder_right):
            if preorder_left > preorder_right:
                return None
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root -inorder_left
            root.left = createTree(preorder_left + 1, preorder_left + size_left_subtree,inorder_left,inorder_root -1)
            root.right = createTree(preorder_left + size_left_subtree +1, preorder_right, inorder_root + 1, inorder_right)
            return root 
        

        n = len(preorder)
        index = {element: i for i,element in enumerate(inorder)}
        return createTree(0,n-1,0,n-1)
    
    def buildTree_106(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return TreeNode()
        
        def tree(l,r,postorders):
            if l >= r:
                return None
            root = TreeNode(postorder[-1])
            pos = inorder.index(root.val)
            
            # left节点在postorder中的位置
            if pos >= 1 and postorders[l,postorders.index(inorder[pos-1])+1]:
                root.left = tree(root,l,postorders.index(inorder[pos-1])+1,postorders[l,postorders.index(inorder[pos-1])+1])

            if pos < ll-1 and postorders[postorders.index(inorder[pos+1]),r]:
                root.right = tree(root,postorders.index(inorder[pos+1]),r,postorders[postorders.index(inorder[pos+1]),r])
            return root
        ll = len(postorder)
        
        return tree(0,ll-1,postorder)
    

