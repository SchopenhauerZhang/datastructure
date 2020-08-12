# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List
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

    def _reverseList_24(self, head: ListNode) -> ListNode:
        """
                定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
            示例:

            输入: 1->2->3->4->5->NULL
            输出: 5->4->3->2->1->NULL

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not head:
            return head
        pre,cur,_next = None,head,head.next

        while _next:
            cur.next,cur,pre,_next = pre,_next,cur,_next.next
        cur.next = pre

        return cur

    def _reverseList_24_eg(self, head: ListNode) -> ListNode:
    
        # 方法1：构建链表的副本 时间复杂度：o(n),空间复杂度：o(n)
        # 双指针：一个指针用作反转后链表的头节点，另一个指针用于遍历原链表
        # if not head:
        #     return None
        # travel = head # 用于遍历原链表
        # reHead = None # 反转后 链表的头节点
        # while travel:
        #     # 这个临时节点就相当于一个副本
        #     temp = ListNode(travel.val)
        #     temp.next = reHead
        #     reHead = temp
        #     travel = travel.next
        # return reHead
    
        # 方法2：三指针：后两个指针用于交换顺序，最前的用于确定遍历位置
        # 特殊情况：链表为空 or 只有一个节点
        if not head or not head.next:
            return head
        # # 特殊情况：只有两个节点
        # if not head.next.next:
        #     A = head
        #     B = head.next
        #     A.next = None
        #     B.next = A
        #     return B
        # 至少3个节点时
        A = head
        B = head.next
        C = head.next.next
        A.next = None    
        while C:
            B.next = A
            A = B
            B = C
            C = C.next
        B.next = A
        return B


