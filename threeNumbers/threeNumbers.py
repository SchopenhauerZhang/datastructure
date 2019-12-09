
class ThreeNumbers(object):
    """
    任意三个数字
    """
    def __init__(self,a:int,b:int,c:int):
        self.numbers = [a,b,c]

    def is_equal(self,a,b,c)->bool:
        """
        三个数字是否相等
        """
        is_eq = True
        if a not in [b,c] and b != c:
            is_eq =  False

        return is_eq


        