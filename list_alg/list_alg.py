class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListAlg(object):
    """
    list相关算法
    """
    def __init__(self,l:list=[]):
        self.lst = l

    def reverse(self)->list:
        """
        列表反转
        """
        length = len(self.lst)
        res = self.lst
        for i in range(length//2):
            res[i],res[length-1-i] = res[length-1-i],res[i]

        return res 

    def offset_numbers(self,offset:int=1,is_iter:bool=True)->list:
        """
        对列表元素偏移指定位数
        """
        if is_iter:
            res = self._offset_iter(offset)
        else:
            res = self._offset(offset)
        
        return res     

    def _offset_iter(self,offset:int=1):  
        """
        通过迭代遍历交换实现偏移
        """
        list_offset = self.lst
        offset_range = offset%len(list_offset)
        for f in range(offset_range):
            tmp = list_offset[len(list_offset)-1]
            for i in range(len(list_offset)-1,0,-1):
                list_offset[i] = list_offset[i-1]
            list_offset[0] = tmp

        return list_offset

    def _offset(self,offset:int=1):
        """
        通过计算将偏移后溢出的元素与未溢出的元素整体交换实现偏移
        """
        return self.lst[len(self.lst)-1-offset:]+self.lst[:len(self.lst)-1-offset]    

    def get_peak(self)->list:
        """
        求取峰值（大于左右两侧）
        """ 
        lst_data = self.lst
        left_data = right_data = lst_data[0]
        res = []

        for i in range(len(lst_data)-2):
            print(left_data,lst_data[i],right_data)
            if left_data < lst_data[i] > right_data:
                res.append(lst_data[i])
            left_data = lst_data[i]
            right_data = lst_data[i+2]

        return res

    def is_mountain_list(self)->bool:
        """
        是否是山脉数组(新增后减)
        eg:
            [1,2,3,6,5,4,3,2]
        """
        is_mt_list = True
        is_rise = True
        is_fall = True

        lst_mt = self.lst
        last_value = lst_mt[0]
        
        for i in lst_mt[1:]:
            if is_rise:
                if i < last_value:
                    is_rise = False
                last_value = i

            if not is_rise and is_fall:
                if i > last_value:
                    is_fall = False
                    break

        if not is_rise and not is_fall:
            is_mt_list = False

        return is_mt_list

    def get_index_from_list_by_sum(self,target:int=0,is_better:bool=True)->list:
        """
        给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
        link:https://leetcode-cn.com/submissions/detail/39467280/
        Notice: 
            1、用变量替换len(nums)会减少内存，但是会增加用时；
            2、range(0,len(nums))比range(len(nums))更高效；
        """
        res = {}
        if is_better:
            res = self._get_index_from_list_by_sum_better(target)
        else:
            res = self._get_index_from_list_by_sum

        return res
            
    def _get_index_from_list_by_sum(self,target:int=0)->list:
        """
        方法与_get_index_from_list_by_sum_better类似，只是耗费了更多的执行用时和内存
        """
        nums = self.lst
        res = {}
        for i in range(0,len(nums)): 
            diff = target-nums[i]
            if diff in res:
                return [res.get(diff), i]
            else:
                res[nums[i]] = i

    def _get_index_from_list_by_sum_better(self,target:int=0)->list: 
        """
        在性能和执行用时上都是完美的
        """
        nums = self.lst
        res = {}  
        for index,value in enumerate(nums):
            if target - value in res is not None:
                return [res.get(target-value),index]
            res[value] = index

    def get_add_two_listNode(self,l1: ListNode, l2: ListNode,is_better:bool=True) -> ListNode:
        """
        给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
        link:https://leetcode-cn.com/submissions/detail/39510474/
        eg:
            (2 -> 4 -> 3) + (5 -> 6 -> 4)=7 -> 0 -> 8
        """
        res = None
        if is_better:
            res = self._get_add_two_listNode_bettter(l1,l2)
        else:
            res= self._get_add_two_listNode(l1,l2)
        
        return res

    def _get_add_two_listNode(self,l1: ListNode, l2: ListNode)->ListNode:    
        """
        还有待进步
        """
        sign = 0
        sum_node = None
        head_node = sum_node
        while l1 and l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_ = val1 + val2 + sign
            if sum_ >= 10:
                sign = sum_ //10
                sum_ = sum_ % 10
            else:
                sign = 0
            if sum_node is None:
                sum_node = ListNode(sum_)
                head_node = sum_node
            else:
                sum_node.next = ListNode(sum_)
                sum_node = sum_node.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                sum_ = l1.val+sign
                if sum_ >= 10:
                    sign = sum_ //10
                    sum_ = sum_ % 10
                else:
                    sign = 0
                sum_node.next = ListNode(sum_)
                sum_node = sum_node.next
                l1 = l1.next
        elif l2:
            while l2:
                sum_ = l2.val+sign
                if sum_ >= 10:
                    sign = sum_ //10
                    sum_ = sum_ % 10
                else:
                    sign = 0
                sum_node.next = ListNode(sum_)
                sum_node = sum_node.next
                l2 = l2.next
        if sign:
            sum_node.next = ListNode(sign)
            sum_node = sum_node.next

        return head_node

    def _get_add_two_listNode_bettter(self,l1: ListNode, l2: ListNode)->ListNode:
        """
        优雅
        """
        a,b,p,carry = l1, l2, None,0
        while a or b:
            val = (a.val if a else 0)+(b.val if b else 0)+carry
            carry,val = val//10 if val>=10 else 0,val%10
            p,p.val = a if a else b,val
            a,b = a.next if a else None,b.next if b else None
            p.next = a if a else b
        
        if carry:
            p.next = ListNode(carry)
            
        return l1

    def find_miss_number(self)->int:
        """
        有一组数字，从1到n，中减少了一个数，顺序也被打乱，放在一个n-1的数组里，请找出丢失的数字
        """
        lst = self.lst
        for i in range(1,len(lst)+1):
            if i not in lst:
                return i

    def delete_repeat_from_list(self,is_del:bool=True)->list:
        """
        删除有序自增列表中的重复元素，只能使用 O(1) 额外空间来完成这个任务
        """
        lst = self.lst
        sentinel = 0
        for i in lst:
            if i != lst[sentinel]:
                lst[sentinel+1] = i
                sentinel += 1

        return lst

    def get_combination_from_list(self,sum_number:int=0)->set:
        """
        已知一个无重复元素的序列,给定一个目标数,找出序列中所有可以使数字和未目标数的组合。
        eg:
            例如序列 [2, 3, 5]， 目标值为8， 最终的组合有
                (2, 3, 3)
                (3, 5)
                (2, 2, 2, 2)
        """
        res_set = set()
        for i in self._get_combination_from_list(sum_number):
            i.sort()
            res_set.add(tuple(i))
        
        return res_set

    def _get_combination_from_list(self,sum_number:int=0)->list:
        """
        获取序列中所有满足条件的组合,存在重复序列
        """
        lst = self.lst
        res_list = []
        for i in lst:
            if sum_number == i:
                res_list.append([i])
                break
            elif sum_number < i:
                continue
            else:
                x = self._get_combination_from_list(sum_number-i)
                for j in x:
                    j.append(i)
                res_list.extend(x)

        return res_list
        


