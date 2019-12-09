
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

    def str_to_digit(self,strs:str='')->int:
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












            
            






