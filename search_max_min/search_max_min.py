
class SearchMaxAndMin(object):
    """
    按照条件查找数组中的元素
    """
    def search(self,list_origin:list)->any:
        """
        找出列表中最大和最小值
        """
        max_item,min_item = list_origin[:2]
        for i in list_origin:
            if i > max_item:
                max_item = i
            if i < min_item:
                min_item = i    
        
        return max_item,min_item
    
    def search_second_item(self,list_origin:list)->any:
        """
        查找list中第二大的元素
        """
        max_item,second_item = list_origin[:2]
        for i in list_origin:
            if i > max_item:
                second_item ,max_item = max_item,i
            elif second_item < i < max_item:
                second_item = i
        
        return  second_item         

    def search_max(self,list_origin:list)->any:
        """
        从先递增后递减的list中找出最大值
        """
        pre_item = list_origin[0]
        for i in list_origin:
            if i < pre_item:
                break
            elif i > pre_item:
                pre_item = i

        return pre_item        
