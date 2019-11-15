import unittest
import reservoir

# 蓄水池算法测试 
class TestReservoir(unittest.TestCase):
    def Reservoir(self):
        r = reservoir.Reservoir()
        r.set_limit(10)
        for i in range(100000):
            r.pool(i)
        print(r.get_pool())

if __name__ == "__main__":
    unittest.main()
