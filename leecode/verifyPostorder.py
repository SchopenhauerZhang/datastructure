class Solution:
    def verifyPostorder(self, sequence: List[int]) -> bool:
        """
        输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

            参考以下这颗二叉搜索树：

                5
                / \
            2   6
            / \
            1   3
            示例 1：

            输入: [1,6,3,2,5]
            输出: false
            示例 2：

            输入: [1,3,2,6,5]
            输出: true

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        # write code here

        if not sequence:
            return True
        root = sequence[-1]
        n = len(sequence)
        # i 确定右子树的第一个值的位置
        for i in range(n):
            if sequence[i] > root:
                break
        # 判断右子树是否全部大于root
        for j in range(i, n-1):
            if sequence[j] < root:
                return False
        
        # 递归左右子树，判断是否都满足
        if i <= 0:
            # 不包含左子树
            left = True 
        else: 
            left = self.verifyPostorder(sequence[:i])
        if i >= n-1: 
            # 不包含右子树
            right = True
        else:
            right = self.verifyPostorder(sequence[i:n-1])
            
        return left and right
    
    def verifyPostorder(self, postorder: List[int]) -> bool:
        '''
        异曲同工之妙,找到第一个右子树的位置，然后遍历左右子树
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
        '''
        def verifyPostorderHelp(start,end):
            if start>=end:
                return True
            else:
                i=start
                while postorder[i]<postorder[end]:i+=1
                m=i
                while postorder[m]>postorder[end]:m+=1
                return m==end and verifyPostorderHelp(start,i-1) and verifyPostorderHelp(i,end-1)
        if len(postorder)<=1:
            return True
        return verifyPostorderHelp(0,len(postorder)-1)