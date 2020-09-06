# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
            给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

            示例 1:

            输入: 1->2->3->4->5->NULL, k = 2
            输出: 4->5->1->2->3->NULL
            解释:
            向右旋转 1 步: 5->1->2->3->4->NULL
            向右旋转 2 步: 4->5->1->2->3->NULL
            示例 2:

            输入: 0->1->2->NULL, k = 4
            输出: 2->0->1->NULL
            解释:
            向右旋转 1 步: 2->0->1->NULL
            向右旋转 2 步: 1->2->0->NULL
            向右旋转 3 步: 0->1->2->NULL
            向右旋转 4 步: 2->0->1->NULL

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/rotate-list
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not head or not head.next or k == 0 or k is None:
            return head
        table = []
        while head:
            table.append(head.val)
            head = head.next
        ll = len(table)
        res = [0]*ll
        for i in range(ll):
            res[(i+k)%ll] = table[i]
        print(res)
        head = None
        for i in res[::-1]:
            p = ListNode(i)
            p.next = head
            head = p
        return head

    def _rotateRight_eg(self, head: ListNode, k: int) -> ListNode:
        """
            精彩
        """
        if not head or not k:
            return head

        listLen = 0
        curr = head
        while curr != None:
            listLen += 1
            curr = curr.next
        k %= listLen

        # k is 2
        slow = fast = head # 1->2->3->4->5, slow and fast is 1
        for i in range(k):
            fast = fast.next # after loop, fast is 3

        
        while fast.next:
            slow = slow.next # after loop, slow is 3
            fast = fast.next # after loop, fast is 5
        # 重新定义链表的头结点
        fast.next = head
        newHead = slow.next
        slow.next = None

        return newHead