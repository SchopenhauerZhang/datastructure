# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        请判断一个链表是否为回文链表。

        示例 1:

        输入: 1->2
        输出: false
        示例 2:

        输入: 1->2->2->1
        输出: true
        """
        pass

    def _isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        if not head.next.next:
            return head.val == head.next.val

        def rever(hl):
            # 反转单链表
            pre = hl
            nil = None
            while pre:
                tmp = pre.next
                pre.next = nil
                nil = pre
                pre = tmp
            return nil
        r = rever(head)
     
        while head  :
            if head.val == r.val:
                r = r.next
                head = head.next  
            else:
                return False
       
        return head == r
# head = ListNode(1)
# head.next  = ListNode(0)
# head.next.next  = ListNode(1)
# head.next.next.next  = ListNode(1)
# head.next.next.next.next  = ListNode(1)
#print(Solution()._isPalindrome(head))

    def _isPalindrome_better(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        def rever(s):
            nil = None
            while s:
                tmp = s.next
                s.next = nil
                nil = s
                s = tmp
            return nil
        slow = rever(slow)
        while slow:
            if slow.val == head.val:
                slow = slow.next
                head = head.next
            else :
                return False
        
        return True






    