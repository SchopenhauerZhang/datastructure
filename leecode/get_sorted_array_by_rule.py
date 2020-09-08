
from typing import List
class Solution:
    def get_sorted_array_by_rule(self, nums: List[int]) -> List[int]:
        """
            给定n个数字，a1a2a3...an,其中每个数字都是大于等于1的正整数，请问这样的数是否可以满足 
            该数比相邻两数相加之和小，从而形成一个数字圆环，an的相邻两数为an-1与a1，数字顺序可以调换，
            如输入为1 7 3 5 最后可以得出一种排列为1 3 7 5 满足数字圆环
        """
        num = sorted(nums)
        if num[-1] < num[-2]+num[-3]:
            num[-1],num[-2] = num[-2],num[-1]
        return num
    
    def change_num_with_even(self,nums):
        """
            给定n个数字，a1a2a3...an,你可以对这个数组执行任意次以下交换操作：

            对于数组中的两个下标i,j（1<=i.j<=n）,如果ai+aj为奇数，那么就可以交换这两个数



            现在允许我们的交换次数不限，求出能够通过若干次操作后得到的数组中字典序最小的一个



            example:

            {A）  

                输入 7 3 5 1    输出 7 3 5 1



            （B）

            输入

            53941 38641 31525 75864 29026 12199 83522 58200 64784 80987

            输出 12199 29026 31525 38641 53941 58200 64784 75864 80987 83522  
             由于要两数相加为奇数，那么我们可以考虑以下三种情况：
            全是奇数 （两数相加为偶数，两两都交换不了）

            全是偶数  （两数相加为偶数，两两都交换不了）

            既有奇数又有偶数 （两数相加既有奇数也有偶数，两两有些能直接交换，有些能间接交换）

            什么意思？理解好这句话，有些能间接交换。例如输入为5 6 4 3 1

            我要让1排在最前面，1和5之间可以直接交换吗？不可以，但是1和5之间可以通过一个偶数（4）来进行间接交换。
        """
        odd = 0
        even = 0
        for i in nums:
            if i%2==0:
                odd += 1
            else:
                even += 1
        if odd and even:
            return sorted(nums)
        return nums

