# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pass

    def _reverseBetween(self, head: ListNode, m: int, n: int):
        def rev(h,m,n):
            l = h
            n = n - m
            m -=1
            
            while m:
                l=l.next
                m -= 1
            pre = l
            l = l.next
            nil = None
            tail = l
            while n and l.next:
                tmp = l.next
                
                l.next = nil
                ll = tmp.next
                tmp.next = l
                l = ll
                nil = tmp
                n -=1 
            pre.next = nil
            tail.next = l

            return h
        return rev(head,m,n)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
h = head
while head:
    print(head.val)
    head = head.next
h = Solution()._reverseBetween(h,2,5)
while h:
    print(h.val)
    h = h.next