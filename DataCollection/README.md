# NAME: DataCollection 
# BY：uiu
# ©️：uiuing.com
# time： 2021-05-10 
---------------------------------------------------------
## 编程语言：Python
## 说明：该模块基于Scrapy框架
## 功能：信息采集
## 数据源：国内权威网站

### 文件说明：
>    /Findbaby/spiders/
            Missing.py       
                ```采集走失儿童信息 & 数据预处理```
            success—case.py  
                ```采集成功案例 & 数据预处理```
            ParticipleAndMatch.py 
                ```地区行政代码处理```
                

>    /Findbaby/
        pipelines.py
            SuccessCasePipeline   
                ```存储成功案例信息```
            MissingPipeline
                ```存储走失儿童信息```
>    其它
        Missing.json        存储文件
        Missing.log         spiders for Missing
        success-case.json   存储文件
        success-case.log    spiders for Success-case

>    被更改文件:
        settings.py
        items.py
        middlewares.py