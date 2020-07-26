# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

        示例 1:

        输入: 1->1->2
        输出: 1->2
        示例 2:

        输入: 1->1->2->3->3
        输出: 1->2->3

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not head or not head.next:
            return head
        tmp = head.val
        pre = head
        p = head.next
        while p:
            if p.val == tmp:
                pre.next = p.next if p else None
            else:
                pre = p
                tmp = p.val
            p = p.next
        return head

    def _deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head