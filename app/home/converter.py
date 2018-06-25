from werkzeug.routing import BaseConverter
import datetime
"""
第一步 定义自定义转化器类   继承BaseConverter
第二步 第一个参数作为正则的匹配规则
第三步 app.url_map.converters['re']=RegexConverter


"""

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*args):
        super().__init__(url_map)
        self.regex=args[0]

     #将匹配到的值转化成python类型
    def to_python(self, value):
        print(value)
        return datetime.datetime.strptime(value,'%Y')
