class Solution:
    res = []
    def letterCombinations(self, digits: str) -> List[str]:
        """
            给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

            给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



            示例:

            输入："23"
            输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            wdnm,“22”不能被正常识别，测试都能过执行过不了
        """
        if not digits:
            return []
        data = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'],
        }
        if len(digits) == 1:
            return data[int(digits)]
        def get(nums,_str):
            
            if not nums:
                return 
            if len(nums) == 1:
                for i in data[int(nums[0])]:
                    print(_str,nums,i)
                    if _str+str(i) not in self.res:
                        self.res.append(_str+str(i))
            else:
                for i in data[int(nums[0])]:
                    get(nums[1:],_str+i)
                        
            return 
        get(list(digits),'')
        return self.res

    def _letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        data = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'],
        }
        if len(digits) == 1:
            return data[int(digits)]
        r = ['']
        for k in digits:
            r = [ i+j for i in r for j in data[int(k)]  ]
        return r
    def _letterCombinations_eg(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        for digit in digits:
            res = [r+char for r in res for char in dic[digit]]
        return res
