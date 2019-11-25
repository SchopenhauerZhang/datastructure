import math

class Matrix(object):
    """
    矩阵相关算法实现
    """
    def diagonal(self,data:list)->any:
        """
        求矩阵的对角线之和
        data :[1,2,3,4,5,6,7,8,9]
        result:1+5+9+3+7
        """
        #TODO 判断输入是否合法
        row_len = math.sqrt(len(data))//1 

        return sum([y for i,y in enumerate(data) if i%(row_len-1) == 0 or i%(row_len+1)==0 ])
        