class Solution:
    def checkRecord(self, s: str) -> bool:
        """
            给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

            'A' : Absent，缺勤
            'L' : Late，迟到
            'P' : Present，到场
            如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

            你需要根据这个学生的出勤记录判断他是否会被奖赏。

            示例 1:

            输入: "PPALLP"
            输出: True
            示例 2:

            输入: "PPALLL"
            输出: False

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/student-attendance-record-i
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s or len(s) <= 2:
            return False if not s or s=='AA' else True

        pre = None
        flag = 0
        from collections import defaultdict
        ct = defaultdict(int)
        for _s in s:
            if _s in ('A','L'):
                if _s == 'L' and pre == _s:
                    flag += 1
                elif _s != pre and pre is not None:
                    pre = None
                    flag = 0
                elif _s == 'L' and pre != _s:
                    pre = _s
                    flag += 1
                

                if flag > 2:
                    return False
                ct[_s] += 1
                if ct['A'] > 1:
                    return False
            else:
                pre = None
                flag = 0

        return True
    
    def _checkRecord_eg(self, s: str) -> bool:
        a = 0
        
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                if a > 1:
                    return False
            elif s[i] == 'L':
                if i < len(s) - 2:
                    if s[i + 1] == 'L' and s[i + 2] == 'L':
                        return False
        return True