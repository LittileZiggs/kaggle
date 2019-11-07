import requests
import json
import csv

headers = {
        "Host": "xszz.e21.cn",
        "Origin": "http://xszz.e21.cn",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://xszz.e21.cn/index.jsp?menuType=diffStdMgr&logDesc=%E5%AD%A6%E7%94%9F%E4%BF%A1%E6%81%AF%E7%AE%A1%E7%90%86",  # 必须带这个参数，不然会报错
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "*"
             }
url = "http://xszz.e21.cn/poorStudent/yj-difficulty-stu!queryStudentBasicInfo.action"
form_data = "start=0&limit=39360&filterValue=&filterTxt=&dateFilter=&startDate=&endDate=&searchForm=&searchFormJm=l%5CygWd%C2%96%C3%8D%C3%9F%C3%9F%C3%9C%C3%9C%C3%98%C3%9D%C2%BA%C2%B1%C3%9B%C3%9B%C3%91%C2%91Wdl_WdfYWd%5EQWd%C2%96%C3%8D%C3%9F%C3%9F%C3%9C%C3%9C%C3%98%C3%9D%C2%B1%C2%B2%C3%93%C3%89%C2%8AWdl_Wdffbggdd%60%60%60%60%60UWdW%5C%7B"
results = requests.post(url, data=form_data, headers=headers)
results.encoding = 'utf-8'
rows = json.loads(results.text)
print(rows['result'])

f = open('data2.csv', 'w')

# 通过文件创建csv对象
#fieldnames = ['id', 'zxzt', 'zt', 'mz', 'zzmm', 'jkzk', 'sfzjlx', 'gj', 'gatqw',
#              'hkxz', 'xzz', 'xm', 'yzbm', 'xmpy', 'xjh', 'xb', 'csrq', 'sfzjh', 'sfjs', 'nj',
#              'jyjd', 'rxny', 'hkszd', 'xz', 'xslb', 'rxfs', 'jg', 'csd', 'lxdh','sfzx', 'cczt', 'xxJbxxId',
#              'njId', 'bjId', 'isJssName', 'xbmc', 'bjmc', 'xxJbxxName', 'xzqhm', 'xxzgbmxzqhm',
#              'isJhdls', 'isSgx', 'xzName', 'minority', 'politicsStatus', 'idCardType', 'nationality', 'categorys']
fieldnames = ['xm', 'xjh', 'sfzjh', 'xxJbxxName', 'nj']
csv_write = csv.DictWriter(f, fieldnames)
for row in rows['result']:
    line = {}
    line['xm'] = row['xm']
    line['xjh'] = row['xjh']
    if 'sfzjh' in row.keys():
        line['sfzjh'] = row['sfzjh']
    else:
        line['sfzjh'] = ""
    line['xxJbxxName'] = row['xxJbxxName']
    line['nj'] = row['nj']
    csv_write.writerow(line)

f.close()