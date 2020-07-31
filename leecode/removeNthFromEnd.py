# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

        示例：

        给定一个链表: 1->2->3->4->5, 和 n = 2.

        当删除了倒数第二个节点后，链表变为 1->2->3->5.
        说明：

        给定的 n 保证是有效的。

        进阶：

        你能尝试使用一趟扫描实现吗？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not head or (not head.next and n == 1):
            return head if not  head else None
        def traverse(r,num):
            if not r :
                return 0
            x = traverse(r.next,num)+1
            if x == num+1:
                r.next = r.next.next
            return x
        p = head
        l = traverse(p,n)
        if l == n:
            # 删除第一个
            return head.next
        return head

    def _removeNthFromEnd_eg(self, head: ListNode, n: int) -> ListNode:
        num = 0                              #统计链表节点总数
        node = head
        while node:
            num += 1
            node = node.next

        node = head
        m = num - n + 1                      #删除倒数第n个节点等价于删除正数第m个节点
        if m > 1:
            for i in range(1 , m - 1):
                node = node.next
            node.next = node.next.next
            return head
        elif m == 1:
            return head.next
        else:
            return head