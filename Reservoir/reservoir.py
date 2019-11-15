import random
# 蓄水池算法(n个元素中找出k个元素)，1/(n-1)*(n-1)/n = 1/n
class Reservoir(object):
    def __init__(self):
        self._pre_k = []
        self._limit = 0
        self._counter = 0

    def counter(self):
        self._counter += 1

    def set_limit(self,limit:int):
        self._limit = limit    

    def pool(self,data):
        """
        抽出limit个元素放入基础池子，limit后面的元素都随机替换池子中的元素
        """
        value = float(data)
        self.counter()
        if len(self._pre_k) < self._limit:
            self._pre_k.append(value)
            return None

        n = random.randint(1,self._counter)
        if n < self._limit:
            self._pre_k[n-1] = data

        return self._pre_k    

    def get_pool(self):
        return self._pre_k









