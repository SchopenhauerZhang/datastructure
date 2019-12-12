
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






















            
            






