
class ListAlg(object):
    """
    list相关算法
    """
    def __init__(self,l:list):
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





