import os

class Tools(object):
    """
    工具类
    """
    def __init__(self):
        pass

    def get_python_code_lines(self,suffix:str='.py',comment:str='#')->str:
        """
        统计代码行数
        """
        count_codes = 0
        for  rooot, dirs, files in os.walk('./',True):
            if type(files) == list:
                for f in files:
                    if f.endswith(suffix):
                        with open(rooot+'/'+f,'r',encoding='utf-8') as lines:
                            for line in lines:
                                line = line.strip()
                                if not line or line.startswith(comment):
                                    continue
                                count_codes += 1
    
        return '遍历{}结尾的文件,代码共计{},其中{}开头的行被忽略'.format(suffix,count_codes,comment)









