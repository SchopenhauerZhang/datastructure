class Solution:
    def get_characters_to_int(self,strs:str)->int:
        """
            meinenghua3 输入【0,1亿)
            eg:五千三百五十一万一千八百二十六 output:53511826
        """
        if not strs or not strs.strip() or strs.strip() == '零':
            return 0
        res = 0
        _res = 0
        ch_int = {
            '零':0,
            '一':1,
            '二':2,
            '三':3,
            '四':4,
            '五':5,
            '六':6,
            '七':7,
            '八':8,
            '九':9,
            '十':10,
            '百':100,
            '千':1000,
            '万':10000,
        }
        for _i in strs:
            if ch_int[_i] >= 10000:
                res*= ch_int[_i]
            else:
                if _i in ('千','百','十'):
                    _res = 1 if res == 0 else res 
                    res += _res * ch_int[_i]
                else:
                    _res = ch_int[_i]

        return res+_res
    
    def get_water_pool(self,nums:List[int])->int:
        """
            meinenghua2 接雨水
        """
        pass
    
    def get_square_colored(self,nums:List[List[int]])->int:
        """
            meinenghua1 着色面积(注意死循环和效率)
        """