
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
            在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

            示例 1:

            输入: 4->2->1->3
            输出: 1->2->3->4
            示例 2:

            输入: -1->5->3->4->0
            输出: -1->0->3->4->5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/sort-list
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            精彩
        """
        list = []
        tem = head
        while tem:
            list.append(tem.val)
            tem = tem.next
        list.sort()
        tem1 = head
        for num in list:
            tem1.val = num
            tem1 = tem1.next
        return head