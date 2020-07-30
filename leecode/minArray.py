class Solution:
    def minArray(self, numbers: list) -> int:
        """
        把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

        示例 1：

        输入：[3,4,5,1,2]
        输出：1
        示例 2：

        输入：[2,2,2,0,1]
        输出：0

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not numbers or len(numbers) <= 2:
            return numbers if not numbers else min(numbers)
        
        
        l,r = 0,len(numbers)-1
        _min = numbers[-1]
        while l < r:
            if numbers[l] < numbers[r]:
            # 旋转点 <= l 
                _min = min(_min,numbers[l])
                r -= 1
            elif numbers[l] > numbers[r]:
            # l <= 旋转点 <= r
                _min = min(_min,numbers[r])
                r -= 1
            else:
            # 旋转点 = l = r
                _min = min(_min,numbers[l])
                l += 1

        return _min

#print(Solution().minArray([10,12,14,17,20,2,7,8,9]))

    def _minArray_eg(self, numbers: list) -> int:
    
        for index in range(1, len(numbers)):
            if numbers[index] < numbers[0]:
                return numbers[index]
        return numbers[0]


    def midArray(self,numbers:list)->int:
        """
        旋转数组的中位数
        """
        if not numbers or len(numbers) <= 2:
            return numbers if not numbers else min(numbers)
        min_pos = 0
        for index in range(1, len(numbers)):
            if numbers[index] < numbers[0]:
                min_pos = index
                break
        
        if min_pos == 0 :
            # 旋转点是最左边
            r = len(numbers)-1
        
        elif min_pos == len(numbers)-1 :
            # 旋转点是最右边
            r = numbers[0]
        else:
            # 旋转点是中间
            r = numbers[min_pos-1] 

        l = min_pos
        _mid = numbers[-1]

        count = len(numbers)//2
        while count:
            if l == len(numbers)-1:
                l = -1
            l += 1
            count -= 1

        _mid = numbers[l] 

        return _mid

print(Solution().midArray([10,12,14,17,20,2,7,8,9]))
print(Solution().midArray([10,12,14,17,7,8,9]))
