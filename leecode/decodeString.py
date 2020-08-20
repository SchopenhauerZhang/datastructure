class Solution:
    def decodeString(self, s: str) -> str:
        """
            给定一个经过编码的字符串，返回它解码后的字符串。

            编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

            你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

            此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

             

            示例 1：

            输入：s = "3[a]2[bc]"
            输出："aaabcbc"
            示例 2：

            输入：s = "3[a2[c]]"
            输出："accaccacc"
            示例 3：

            输入：s = "2[abc]3[cd]ef"
            输出："abcabccdcdcdef"
            示例 4：

            输入：s = "abc3[cd]xyz"
            输出："abccdcdcdxyz"

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/decode-string
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s or '[' not in s:
            return s if s else ''
        ll = len(s)
        l = ll-1
        sl = list(s) 
        temp = []
        res = ''
        is_flag = 0
        while l >= 0:
            if sl[l] == ']':
                is_flag += 1
                temp.append(sl[l])
            elif is_flag == 0 and sl[l] != ']':
                res = sl[l]+ res 
            elif is_flag and sl[l] != '[' :
                temp.append(sl[l])
            elif sl[l] == '[':
                is_flag -= 1
                if is_flag == 0:
                    _l = l
                    long = len(temp) - temp[::-1].index(']') 
                    _l-=1
                    _num = sl[_l]
                    _l -= 1
                    while _l >=0:
                        if sl[_l] not in ('0','1','2','3','4','5','6','7','8','9'):
                            break
                        else:
                            print(sl[_l])
                            _num = sl[_l]+_num
                        _l -= 1
                    print(long,temp,_num)
                    res = ''.join(temp[long:][::-1]) * int(_num) +res
                    temp = temp[:long-1]
                    l = _l 
                    continue
                else:
                    _l = l
                    long = len(temp) - temp[::-1].index(']') 
                    
                    _l-=1
                    _num = sl[_l]
                    _l -= 1
                    while _l >=0:
                        if sl[_l] not in ('0','1','2','3','4','5','6','7','8','9'):
                            break
                        else:
                            _num = sl[_l]+_num
                        _l -= 1
                    _res = ''.join(temp[long:][::-1]) * int(_num) 
                    
                    
                    temp = temp[:long-1]
                    temp.append(_res)
                    l = _l 
                    continue
            else:
                res = sl[l]+res

            l -= 1
        return res

    def _decodeString_eg(self, s: str) -> str:
        return eval(re.sub("([')])([0-9'])",r"\1+\2",re.sub("(\d)\[",r"\1*(",re.sub("([a-zA-Z]+)",r"'\1'",s)).replace("]",")"))) if s else ""