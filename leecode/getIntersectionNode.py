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