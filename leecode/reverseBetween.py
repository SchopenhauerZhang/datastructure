# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _reverseBetween(self, head: ListNode, m: int, n: int):
        if m ==n :
            return head
        def rev(h,m,n):
            l = h
            n = n - m + 1
            if m!= 1:
                while m >1:
                    pre = l
                    l=l.next
                    m -= 1
            else:
                pre = None
            
            nil = None
            tail = l
            
            while n  and l :
                tmp = l.next
                l.next = nil
                nil = l
                l = tmp
                n -=1 
            if pre:
                pre.next = nil
            else:
                h = nil
            tail.next = l

            return h
        return rev(head,m,n)


# head = ListNode(3)
# head.next = ListNode(5)
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# h = head
# while head:
#     print(head.val)
#     head = head.next
# h = Solution()._reverseBetween(h,2,4)
# while h:
#     print(h.val)
#     h = h.next

    def _reverseBetween(self, head: ListNode, m: int, n: int):
        dummy = p = q = ListNode(None)
        cur_len = 0
        while head:
            cur_len += 1
            cur = head
            head = head.next
            cur.next = None
            if cur_len < m:
                p.next = cur
                p = p.next
            elif cur_len == m:
                p.next = q = cur
            elif cur_len <= n:
                cur.next = p.next
                p.next = cur
            else: 
                q.next = cur
                cur.next = head
                break
        return dummy.next