# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        1,2,3,4,5
        反转一个单链表。

        示例:

        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL
        进阶:
        你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/reverse-linked-list
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not head:
            return None
        if not head.next:
            return head
        headNode = self.reverseList(head.next)#4
        head.next.next = head#3
        head.next = None
        return headNode

    #法1：迭代
    def _reverseList(self, head: ListNode) -> ListNode:
        p = head 
        rev = None
        while p:
            rev,rev.next,p = p,rev,p.next
        return rev

    def _reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev



