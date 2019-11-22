
class YanghuiTriangle(object):
    """
    打印杨辉三角的类
    """
    def triangle(self,n):
        """
        打印杨辉三角的执行函数
        """
        if n == 1:
            print([1])
            lst = [1]
        elif n == 2:
            print([1,1])
            lst = [1,1] 
        else:
            lst = [1]
            p_lst = self.triangle(n-1)
            for i in range(len(p_lst)-1):
                lst.append(p_lst[i]+p_lst[i+1])
            lst.append(1)
            print(lst)

        return lst    


