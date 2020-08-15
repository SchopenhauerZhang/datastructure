# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
        示例：

        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val<=l2.val:
            h = l1
            h.next = self.mergeTwoLists(l1.next, l2)
        else:
            h = l2
            h.next = self.mergeTwoLists(l1, l2.next)
        return h
        
    def _mergeTwoLists_eg(self, l1: ListNode, l2: ListNode) -> ListNode:
        r_list = []
        while l1 and l2:
            if l1.val < l2.val:
                r_list.append(l1.val)
                l1 = l1.next
            else:
                r_list.append(l2.val)
                l2 = l2.next
        for rest_l in [l1, l2]:
            while rest_l:
                r_list.append(rest_l.val)
                rest_l = rest_l.next
        if  r_list:
            r_list_node = ListNode(val=r_list[0])
            temp_node = r_list_node
            for ind in range(1, len(r_list)):
                num = r_list[ind]
                temp_node.next = ListNode(val=num)
                temp_node = temp_node.next        
            return r_list_node
        else:
            return None
    
    def _mergeTwoLists_25(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
                输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

        示例1：

        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        限制：

        0 <= 链表长度 <= 1000

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not l1 or not l2:
            return l1 if not l2 else l2
        l,r = l1,l2
        h=None
        pre = None
        while l and r:
            if l.val < r.val:
                if h is None:
                    h = l
                    pre = h
                else:
                    h.next = l
                l = l.next
            else:
                if h is None:
                    h = r
                    pre = h
                else:
                    h.next = r
                r = r.next
        h.next = l if not r else r
        return pre

    def _mergeTwoLists_25_eg(self, l1: ListNode, l2: ListNode) -> ListNode:
        hair = ListNode(None)
        p1 = hair
        while l1 and l2:
            if (l1.val >= l2.val):
                p1.next = l2
                l2 = l2.next
            else:
                p1.next = l1
                l1 = l1.next
            p1 = p1.next
        p1.next = l1 if not l2 else l2
        return hair.next
