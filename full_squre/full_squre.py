
class FullSqure(object):
    """
    求完全平方数
    """
    def getFromZeroToMax(self, max_range:int=10000)->list:
        """
        求max_range 范围内的所有完全平方数
        """
        res = []
        for i in range(max_range//2):
            if i*i <= max_range:
                res.append(i)

        return res
    
    def getFromMaxToZero(self,max_range:int=10000)->list:
        """
        求max_range内的所有完全平方数（从max开始进行开平方校验）
        """
        res = []
        
        return res

