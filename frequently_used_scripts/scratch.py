import csv
import json
import requests
import datetime

postUrl = 'http://xqjy.e21.cn/childmng/childmng.action'
# payloadData数据
payloadData = {"map": {"method": "queryChildListByCon", "params": {"javaClass": "java.util.ArrayList", "list": [{
                                                                                                                    "map": {
                                                                                                                        "xm": "",
                                                                                                                        "xbm": "",
                                                                                                                        "mzm": "",
                                                                                                                        "hkxz": "",
                                                                                                                        "dszn": "",
                                                                                                                        "lset": "",
                                                                                                                        "jcwg": "",
                                                                                                                        "cjye": "",
                                                                                                                        "ge": "",
                                                                                                                        "sfzjhm": "",
                                                                                                                        "jgmc": "",
                                                                                                                        "xzqdm": ""},
                                                                                                                    "javaClass": "java.util.HashMap"}]},
                       "pm": {"javaClass": "com.neusoft.education.edp.client.PageManager", "pageSize": 15974,
                              "pageNo": "1", "totalCount": -1,
                              "filters": {"javaClass": "com.neusoft.education.edp.client.QueryFilter",
                                          "parameters": {"javaClass": "java.util.HashMap", "map": {}}},
                              "resPojoName": ""}}, "javaClass": "java.util.HashMap"}
# 请求头设置
payloadHeader = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "clientType": "json",
    "Connection": "keep-alive",
    "Content-Length": "631",
    "Content-Type": "text/plain;charset=UTF-8",
    "Cookie": "JSESSIONID=SAZdowWTResgzYc0Gfpa1wIowhSryBEJiCK6dnkPnl0N001aMFPn!-1020405545",
    "Host": "xqjy.e21.cn",
    "Origin": "http://xqjy.e21.cn",
    "Referer": "http://xqjy.e21.cn/forward.action?path=/portal/portal&p=childmng&menu_id=3001",
    "render": "json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
# 下载超时
timeOut = 30
# 代理
proxy = "183.12.50.118:8080"
proxies = {
    "http": proxy,
    "https": proxy,
}
r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
dumpJsonData = json.dumps(payloadData)
#print(f"dumpJsonData = {dumpJsonData}")
#res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut, proxies=proxies,
#                    allow_redirects=True)
# 下面这种直接填充json参数的方式也OK
# res = requests.post(postUrl, json=payloadData, headers=header)
# print(f"responseTime = {datetime.datetime.now()}, statusCode = {r.status_code}, res text = {r.text}")

rows = json.loads(r.text)
print(f"rows = {rows['list']}")
# 创建文件对象
f = open('data.csv', 'w')

# 通过文件创建csv对象
fieldnames = ['MZ', 'JHRZJ', 'ZJLX', 'SFZJH', 'XXMC', 'JHRSFZH', 'CSRQ', 'XM', 'BJMC',
              'XB', 'DSMC', 'SSZGJYXZMC', 'JHRXM', 'SJMC', 'ROWNUM', 'XQ_YE_JBXX_ID', 'RYRQ', 'YEXJH']
csv_write = csv.DictWriter(f, fieldnames)

# csv_write.writerow(rows[0].keys())
for row in rows['list']:
    # csv_write.writerow(row['map']['MZ'],
    #                    row['map']['JHRZJ'],
    #                    row['map']['ZJLX'],
    #                    row['map']['SFZJH'],
    #                    row['map']['XXMC'],
    #                    row['map']['JHRSFZH'],
    #                    row['map']['CSRQ'],
    #                    row['map']['XM'],
    #                    row['map']['BJMC'],
    #                    row['map']['XB'],
    #                    row['map']['DSMC'],
    #                    row['map']['SSZGJYXZMC'],
    #                    row['map']['JHRXM'],
    #                    row['map']['SJMC'],
    #                    str(row['map']['ROWNUM']),
    #                    row['map']['XQ_YE_JBXX_ID'],
    #                    row['map']['RYRQ'],
    #                    row['map']['YEXJH'])
    csv_write.writerow(row['map'])

# 关闭打开的文件
f.close()