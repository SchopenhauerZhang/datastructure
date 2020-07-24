class Solution:
    def countAndSay(self, n: int) -> str:
        """
        给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

            注意：整数序列中的每一项将表示为一个字符串。

            「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

            1.     1
            2.     11
            3.     21
            4.     1211
            5.     111221
            第一项是数字 1

            描述前一项，这个数是 1 即 “一个 1 ”，记作 11

            描述前一项，这个数是 11 即 “两个 1 ” ，记作 21

            描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211

            描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

             

            示例 1:

            输入: 1
            输出: "1"
            解释：这是一个基本样例。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/count-and-say
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        n_tmp = 1
        tmp = []
        tmp.append('1')
        while n_tmp < n:
            data = tmp.pop()
            _tmp = []
            _tmp_str = ''

            for i in range(len(data)-1,-1,-1):
                if not _tmp:
                    _tmp.append(str(data[i]))
                elif _tmp[-1] == data[i]:
                    _tmp.append(str(data[i]))
                else:
                    _tmp_str = str(len(_tmp))+_tmp[-1]+_tmp_str
                    _tmp = [str(data[i])]
            
            if _tmp:
                _tmp_str = str(len(_tmp))+_tmp[-1]+_tmp_str
           
            tmp.append(_tmp_str)
            n_tmp += 1
            
        return tmp.pop()

# print(Solution().countAndSay(1))
# print(Solution().countAndSay(2))
# print(Solution().countAndSay(3))#21
# print(Solution().countAndSay(4))#1211
# print(Solution().countAndSay(5))#111221
# print(Solution().countAndSay(6))

    def _countAndSay_eg(self, n: int) -> str:
        nums = ['1']
        for i in range(n-1):
            count = 1
            num_temp = []
            nums.append('')
            #这样就可以执行到最后一个数字
            for j in range(len(nums)-1):
                if nums[j] == nums[j+1]:
                    count += 1
                else:
                    num_temp.append(str(count))
                    num_temp.append(nums[j])
                    count=1
            nums = num_temp
        return ''.join(nums)
