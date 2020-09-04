# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            编写一个程序，找到两个单链表相交的起始节点。
        """

        if not headA or not headB:
            return None
        
        tmp = []
        while headA :
            tmp.append(headA.val)
            headA = headA.next
        while headB :
            if headB.val in tmp:
                return True
            headB = headB.next

        return False

    def _getIntersectionNode_eg(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
    
    def getIntersectionNode_52(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
            输出：Reference of the node with value = 8
            输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
                输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
            输出：null
            输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
            解释：这两个链表不相交，因此返回 null。
             

            注意：

            如果两个链表没有交点，返回 null.
            在返回结果后，两个链表仍须保持原有的结构。
            可假定整个链表结构中没有循环。
            程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

            输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
            输出：Reference of the node with value = 2
            输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        h1,h2 = headA,headB 
        while h1 != h2:
            h1 = h1.next if h1 else headB
            h2 = h2.next if h2 else headA

        return h1
    
    def _getIntersectionNode_52(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1 = headA
        node2 = headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1