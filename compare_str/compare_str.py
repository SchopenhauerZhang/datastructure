
class CompareStr(object):
    """
    比较字符串
    """
    def ignore_case(self,string_A:str,string_B:str):
        """
        使用lower比较
        """
        if string_A.lower()) == string_B.lower():
            return True

        return False    

    def ignore_case_self_compare(self,string_A:str,string_B:str):
        """
        通过比较字节码进行比较
        """
        is_equal = False

        if string_A == string_B:
            is_equal = True
        else:
            is_equal =  self._sum_bytes_numbers(string_A) == self._sum_bytes_numbers(string_B)

        return is_equal 

    def _sum_bytes_numbers(self,string_A:str):
        """
        迭代sum字符串的值并返回int
        """
        back_sum = 0
        for i in string_A:
            back_sum += ord(i)

        return  back_sum  
