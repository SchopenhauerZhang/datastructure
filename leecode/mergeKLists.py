# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
            给你一个链表数组，每个链表都已经按升序排列。

            请你将所有链表合并到一个升序链表中，返回合并后的链表。

             

            示例 1：

            输入：lists = [[1,4,5],[1,3,4],[2,6]]
            输出：[1,1,2,3,4,4,5,6]
            解释：链表数组如下：
            [
            1->4->5,
            1->3->4,
            2->6
            ]
            将它们合并到一个有序链表中得到。
            1->1->2->3->4->4->5->6
            示例 2：

            输入：lists = []
            输出：[]
            示例 3：

            输入：lists = [[]]
            输出：[]
             

            提示：

            k == lists.length
            0 <= k <= 10^4
            0 <= lists[i].length <= 500
            -10^4 <= lists[i][j] <= 10^4
            lists[i] 按 升序 排列
            lists[i].length 的总和不超过 10^4

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            输出超出限制
        """
        if not lists or (len(lists) == 1 and not lists[0]):
            return None
        if len(lists) == 1 and not lists[0].next:
            return lists[0]
        res = []
        head = ListNode(-1)
        h = head
        ll = len(lists)
        k = 0
        pos = 0
        
        
        while lists:
            i = 0
            if lists[i]:
                cur = ListNode(lists[i].val)
                break
            else:
                del lists[i]
                
            
        if not lists or not lists[0]:
            return None
        if len(lists) == 1 and not lists[0].next:
            return lists[0]
        while cur:
            ll = len(lists)
            for i in range(ll):
                if lists[i] is None:
                    continue
                print(lists[i].val,cur.val)
                if lists[i].val < cur.val:
                    cur = lists[i]
                    pos = i
            h.next = cur
            tmp = lists[pos].next
            if tmp is not None:
                lists[pos] = tmp
            else:
                del lists[pos]
                if not lists:
                    break
                while lists:
                    i = 0
                    if lists[i]:
                        tmp = ListNode(lists[i].val)
                        break
                    else:
                        del lists[i]
                if not lists:
                    break
                tmp = lists[0]
                pos = 0
                
            cur = tmp
            h = h.next
        return head.next
    
    def _mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or (len(lists) == 1 and not lists[0]):
            return None
        if len(lists) == 1 and not lists[0].next:
            return lists[0]
        res = []
        i = 0
        while lists:
            if not lists[i]:
                del lists[i]
                continue
            res.append(lists[i].val)
            lists[i] = lists[i].next
        print(res)
        head = ListNode(-1)
        p = head

        for i in sorted(res):
            p.next = ListNode(i)
            p = p.next
        return head.next

    def _mergeKLists_eg(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length == 0:
            return None
        elif length == 1:
            return lists[0]
        
        dummy = ListNode(0)
        nodes = []
        
        for linked_l in lists:
            if linked_l != None:
                p = linked_l
                while p:
                    nodes.append(p)
                    p = p.next
        
        nodes.sort(key=self.get_key)
        p = dummy
        for n in nodes:
            p.next = n
            p = p.next
        
        return dummy.next
    
    def get_key(self, obj):
        return obj.val

            