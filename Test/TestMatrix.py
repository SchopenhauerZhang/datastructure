import unittest 
from matrix.matrix import Matrix
class TestMatrix(unittest.TestCase):
    def diagonal(self):
        m = Matrix()
        return self.assertEquals(m.diagonal([1,2,3,4,5,6,7,8,9]),25)

if __name__ == "__main__":
    unittest.main()
