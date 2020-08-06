# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
            给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

            为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

            说明：不允许修改给定的链表。

             

            示例 1：

            输入：head = [3,2,0,-4], pos = 1
            输出：tail connects to node index 1
            解释：链表中有一个环，其尾部连接到第二个节点。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        f,s=head.next,head
        while f and f.next:
            f = f.next
            s = s.next
            if f == s:
                break
        s = f
        while f != s:
            f= f.next
            s = s.next
         

        return s
    
    def _detectCycle_eg(self, head: ListNode) -> ListNode:
        nodes = set()
        while head:
            if head.next in nodes:
                return head.next
            nodes.add(head)
            head = head.next
        return None