import random

class Ints(object):
    """
    数字、整型相关操作
    """
    def __init__(self):
        pass

    def get_count_one_from_binary(self,int_data:int=0)->int:
        """
        统计数字的二进制数中1的个数
        """
        count = x = 0
        while int_data:
            rrr = random.randrange(3)
            if rrr == 1:
                int_data,x = int_data>>1,int_data%2 
            elif rrr == 2:
                int_data,x = int_data//2,int_data%2 
            else:
                int_data,x = int_data>>1,int_data&1 

            if x == 1:
                count +=1

        return count
