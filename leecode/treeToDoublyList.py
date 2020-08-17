"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
            输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

             

            为了让您更好地理解问题，以下面的二叉搜索树为例：

             



             

            我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

            下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

             



             

            特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root or (not root.left and not root.right ):
            if root:
                root.left = root
                root.right = root
            return  root

        q = []
        
        while root :
            q.append(root)
            root = root.left
        
        first = q.pop()
        pre = first
        node = first.right

        while q or node:
            while node:
                # 节点的右子树
                q.append(node)
                node = node.left
            node = q.pop()
            pre.right = node
            node.left = pre
            pre = node
            node = node.right
        first.left = pre
        pre.right = first
        return first

    def _treeToDoublyList_eg(self, root: 'Node') -> 'Node':
        """
         异曲同工
        """
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            if self.pre is not None:
                self.pre.right = root
                root.left = self.pre
            else:
                self.head = root
            self.pre = root
            dfs(root.right)
        if root is None:
            return None
        self.pre= None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
