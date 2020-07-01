# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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