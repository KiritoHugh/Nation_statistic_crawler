import requests
import time
import pprint

# 用来获取 时间戳
def gettime():
    return int(round(time.time() * 1000))

def nation_stat(valueocode):
        # 用来自定义头部的
    headers = {}
    # 用来传递参数的
    keyvalue = {}
    # 目标网址(问号前面的东西)
    url = 'http://data.stats.gov.cn/easyquery.htm'

    # 头部的填充
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    # 下面是参数的填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"'+valueocode+'"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.get(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    # print( r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r = s.get(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    # print(r.status_code)
    # 打印构造的url
    print( r.url)
    # 打印返回的数据
    # print(r.text)
    result = {}
    true = True
    false = False
    result = eval(r.text)
    # pprint.pprint(result)
    returndata = result['returndata']
    datanodes = returndata['datanodes']
    return datanodes