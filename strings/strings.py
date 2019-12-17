
class Strings(object):
    """
    字符串操作类
    """
    def __init__(self,strings:str=''):
        self.s = strings

    def is_palindrome(self,is_strict:bool=True)->bool:
        """
        验证是否是回文串
            1) 严格模式,比如'abccba'
            2) 正常模式,比如'123A man, a plan, a canal: Panama321'
        """
        is_not_palindrome = True
        if self.s:
            string = self.s 
            if is_strict:
                is_not_palindrome = self._is_strict_palindrome(string)
            else:
                is_not_palindrome = self._is_not_strict_palindrome(string)
        else:
            is_not_palindrome = False

        return is_not_palindrome

    def _is_strict_palindrome(self,string:str='')->bool:
        is_not_palindrome = True
        l_str = len(string)

        for i in range(l_str//2):
            if string[i] == string[l_str-1-i]:
                continue
            else:
                is_not_palindrome = False
                break  

        return is_not_palindrome   

    def _is_not_strict_palindrome(self,string:str='')->bool:
        is_not_palindrome = True
        string_cpy = []

        for i in string:
            if i.isdigit() or i.isalpha():
                string_cpy.append(i)

        l_str_cpy = len(string_cpy) 

        for i in range(l_str_cpy//2):
            if string_cpy[i].lower() != string_cpy[l_str_cpy-1-i].lower():
                is_not_palindrome = False
                break

        return is_not_palindrome    
    
    def reverseWords(self,string:str='', is_strict:bool=True)->str:
        """
        反转【句子中的】单词
        """
        words = []
        string = string.strip()
        word = ''
        for i in string:
            if i.isalpha() or i.isdigit():
                word += i
            else:
                words.append(word)
                word = ''

        if word:
            words.append(word)

        if is_strict:
            res = self._is_strict_reverse_words(words)
        else:
            res = self._is_not_strict_reverse_words(words)

        return res
    
    def _is_strict_reverse_words(self,words:list=[])->list:
        """
        反转单词的顺序并且反转单词中字符的顺序
        eg:
            this is a pen => nep a si siht
        """
        for i,y in enumerate(words):
            words[i] = words[i][::-1]

        return words[::-1]

    def _is_not_strict_reverse_words(self,words:list=[])->list:
        """
        反转单词的顺序
        eg:
            this is a pen => pen a is this
        """
        return words[::-1]

    def get_str_to_digit(self,strs:str='')->int:
        """
        将字符串转为数字
        """
        res = 0
        res_10 = lambda res: res*10

        for i in strs:
            if i.isdigit():
                res = res_10(res)
                res += int(float(i))
            else:
                break

        return res
    
    def get_first_pos_from_str(self,str1:str='',character:str='')->int:
        """
        找到字符在字符串中第一次出现的位置【不使用字典】
        """
        res_pos = -1
        for index,value in enumerate(str1):
            if value.lower() == character.lower():
                res_pos = index
                break
        
        return res_pos

    def get_product_from_two_strs(self,str1:str='0',str2:str='0')->str:
        """
        有两个字符串，str1,str2，内容为数值，数值均大于0请编写算法计算两个字符串相乘的结果，不可以使用大数据类型，不可以把字符串直接转成整数来处理
        """
        itera_str1 = str1
        itera_str2 = str2
        sign = 0
        res_str3 = ''
        for i in range(len(itera_str1),0,-1):
            for j in range(len(itera_str2),0,-1): 
                product = int(float(i))*int(float(j))+sign
                product,sign = product%10,product//10
                res_str3 = str(product) + res_str3
        
        if sign:
            res_str3 = str(sign) + res_str3
        
        return res_str3

    def get_sum_from_two_strs(self,str1:str='0',str2:str='0')->str:
        """
        有两个字符串，str1,str2，内容为数值，数值均大于0请编写算法计算两个字符串相加的结果，不可以使用大数据类型，不可以把字符串直接转成整数来处理
        """
        itera_str1 = str1
        itera_str2 = str2
        max_len = max(len(itera_str1),len(itera_str2))

        while max_len!= len(itera_str1) or max_len!= len(itera_str2):
            if max_len!= len(itera_str1):
                itera_str1 = '0'+itera_str1
            elif max_len!= len(itera_str2):
                itera_str2 = '0'+itera_str2

        sign = 0
        res_str3 = ''
        for i in range(len(itera_str1)-1,-1,-1):
            product = int(float(itera_str1[i]))+int(float(itera_str2[i]))+sign
            product,sign = product%10,product//10
            res_str3 = str(product) + res_str3
        
        if sign:
            res_str3 = str(sign) + res_str3
        
        return res_str3

    def get_words_from_strs(self,string:str='')->list:
        """
        从字符串里提取单词，例如”this is a book“，将单词放到列表里，要求是不能使用split函数
        """
        res_list = []
        word = ''
        for i in string:
            if i.strip():
                word += i
            elif word.strip():
                res_list.append(word)
                word = ''

        if word.strip():
            res_list.append(word)

        return res_list
    
    def get_num_sequence(self,string:str='',son_string:str='',is_return_list:bool=True,is_strict:bool=True)->int:
        """
        给定一个字符串S和一个字符串T，计算S的子序列中T出现的次数。
        """
        set_string = self._set_get_pos_by_son_string_from_string(string)
        list_son_string_sequence = self._itera_get_son_string_sequence_from_string(set_string,son_string,0,len(string))
        # 剔除不符合规范的子串（比如顺序倒置）
        if is_strict:
            for index,_list_son_string in enumerate(list_son_string_sequence):
                is_strict = True
                pre_character = _list_son_string[0]
                for i in _list_son_string:
                    if pre_character < i:
                        is_strict = False
                        break
                    else:
                        pre_character = i
                if not is_strict:
                    del list_son_string_sequence[index]

        return len(list_son_string_sequence) if not  is_return_list else list_son_string_sequence

    def _itera_get_son_string_sequence_from_string(self,set_character_pos:set='',son_string:str='',start_pos:int=0,end_pos:int=-1)->list:
        """
        从长串中迭代获取子串序列，获取到所有可能的结果
        """
        list_character_pos_by_son_string_from_set_character_pos = []

        if start_pos < len(son_string):
            character = son_string[start_pos]

            if character in set_character_pos:

                for character_pos in set_character_pos[character]:
                    if character_pos < start_pos:
                        continue
                    if character == son_string[len(son_string)-1]:
                        list_character_pos_by_son_string_from_set_character_pos.append([character_pos])
                    else:
                        list_character_pos = self._itera_get_son_string_sequence_from_string(set_character_pos,son_string,start_pos+1,end_pos)                     
                        for pos in list_character_pos:
                            pos.append(character_pos)

                        list_character_pos_by_son_string_from_set_character_pos.extend(list_character_pos)

        return list_character_pos_by_son_string_from_set_character_pos
    
    def _set_get_pos_by_son_string_from_string(self,string:str='')->set:
        """
        将字符串转为集合
        """
        set_from_string_res = {}
        for index,value in enumerate(string):
            if value in set_from_string_res:
                set_from_string_res[value].append(index)
            else:
                set_from_string_res[value] = [index]

        return set_from_string_res


            
            






