# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
            给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

            你应当保留两个分区中每个节点的初始相对位置。

            示例:

            输入: head = 1->4->3->2->5->2, x = 3
            输出: 1->2->2->4->3->5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/partition-list
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if  not head or not head.next or x is None:
            return head
        p1,p2 = ListNode(-1),ListNode(-1)
        p1.next = head
        l,r= p1,p2
        while p1.next:
            if p1.next.val < x:
                p1 = p1.next
            else:
                p2.next = p1.next
                p2 = p2.next
                p1.next = p1.next.next
                p2.next = None
        p1.next = r.next
        return l.next
    
    def _partition_eg(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next


        