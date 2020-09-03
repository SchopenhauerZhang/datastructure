from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        """
            示例 2：

        输入：[3,5,5]
        输出：false
        示例 3：

        输入：[0,3,2,1]
        输出：true
         

        提示：

        0 <= A.length <= 10000
        0 <= A[i] <= 10000 

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/valid-mountain-array
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not A or len(A) < 3:
            return False
        flag = False
        for i in range(1,len(A)):
            if i == 1 and not flag and A[i] < A[i-1]:
                return False
            if not flag and A[i] > A[i-1]:
                continue
            elif not flag and A[i] < A[i-1]:
                flag = True
            elif flag and A[i] < A[i-1]:
                continue
            else: 
                return False
        return True if flag == True else False
    
    def _validMountainArray_eg(self, A: List[int]) -> bool:
        
        # edge case
        size = len(A)
        if size < 3:
            return False
        
        # if size == 3:
        #     if A[0] >= A[1] or A[2] >= A[1]:
        #         return False
        
        # find the biggest
        # maxNum = 0
        # maxNumIndex = 0
        # for i in range(size):
        #     if A[i] > maxNum:
        #         maxNum = A[i]
        #         maxNumIndex = i
                
        maxNumIndex = A.index(max(A))
                
        # edge case
        if maxNumIndex == size-1 or maxNumIndex == 0:
            return False
              
        # check the pattern
        for i in range(maxNumIndex):
            if(A[i] >= A[i+1]):
                return False
        
        for i in range(maxNumIndex+1, size, 1):
            if(A[i] >= A[i-1]):
                return False
            
        return True