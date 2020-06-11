# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

        k 是一个正整数，它的值小于或等于链表的长度。

        如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
        示例：

        给你这个链表：1->2->3->4->5

        当 k = 2 时，应当返回: 2->1->4->3->5

        当 k = 3 时，应当返回: 3->2->1->4->5
        说明：
        你的算法只能使用常数的额外空间。
        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
        """
        pass

    def _reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        if k <= 1 :
            return head
        
        def _reverse(s1,e):
            s = s1
            _next = s
            nil = None
            while s != e:
                _next = s.next
                s.next = nil
                nil = s
                s = _next 
            return nil

        start = end = head
        for i in range(k):
            if end is None:
                return head
            end = end.next

        reverse_head = _reverse(start,end)#左闭右开

        start.next = self._reverseKGroup(end,k)

        return reverse_head
        
    def _reverseKGroup_eg(self, head: ListNode, k: int) -> ListNode:
        dummy = pre_head = ListNode(0)
        start = end = head

        while True:
            count = 0
            while end and count != k:
                end, count = end.next, count + 1
            if count < k:
                return dummy.next
            pre, cur = end, start
            for _ in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            pre_head.next = pre

            pre_head = start
            start = end
