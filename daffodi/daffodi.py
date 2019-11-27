
class Daffodi(object):
    """
    寻找水仙花数 x = i**3 + y**3 + z**3
    i，y，z分别是x的三位
    """
    def get(self):
         for i in range(100,999): 
            daf = i
            sum_i = 0 
            while daf > 0:
                sum_i += (daf % 10)**3
                daf //= 10
            if sum_i == i:
                print("水仙花数",i)

