
import subprocess,json,time
class Gx_spider(object):
    """
    http://zjt.st.zakww.com/gxslExam/api.do?pa=examinee.subject.list.forward&userId=o1eidc8k5u2tShEI444EpatOAwvonuMN
    公共类+专业C类
    """
    def __init__(self):
        super().__init__()
        self.spider_url()

    def spider_url(self):
        fhand = self.get_txt_handle()
        datas = set()
        for i in range(710):
            ec2_info = subprocess.Popen(["bash","/Users/schopenhauerzhang/code/pythonCode/datastructure/spider/guangxi/guangxi.sh"], stdout=subprocess.PIPE)
            info,b = ec2_info.communicate()
            
            info = str(info,encoding = "utf-8")
            dict_response = json.loads(info)
            dres_dataata  = dict_response['result']
            if not dres_dataata.get('content',None):
                continue

            if dres_dataata['content'] not in datas:
                datas.add(dres_dataata['content'])
                _optios = ''
                for i in dres_dataata['options']:
                    _optios+= i['letter']+':'+i['content']+','
                fhand.write('公共知识'+','+dres_dataata['questionNo']+','+dres_dataata['content']+','+dres_dataata['rightAnswer']+','+_optios+','+'\n')
            print(i,len(datas))
        for i in range(380):
            ec2_info = subprocess.Popen(["bash","/Users/schopenhauerzhang/code/pythonCode/datastructure/spider/guangxi/guangxi_C.sh"], stdout=subprocess.PIPE)
            info,b = ec2_info.communicate()
            
            info = str(info,encoding = "utf-8")
            dict_response = json.loads(info)
            dres_dataata  = dict_response['result']
            if not dres_dataata.get('content',None):
                continue

            if dres_dataata['content'] not in datas:
                datas.add(dres_dataata['content'])
                _optios = ''
                for i in dres_dataata['options']:
                    _optios+= i['letter']+':'+i['content']+','
                fhand.write('专业c类'+','+dres_dataata['questionNo']+','+dres_dataata['content']+','+dres_dataata['rightAnswer']+','+_optios+','+'\n')
            print(i,len(datas))
        fhand.close()
    def get_txt_handle(self):
        f = open('/Users/schopenhauerzhang/code/pythonCode/datastructure/spider/guangxi/20200917_.csv','a+')
        f.write('题目类型,题目编号,题干,参考答案,选项\n')
        return f
Gx_spider()
