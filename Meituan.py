import requests
import re
import csv
from bs4 import BeautifulSoup
url = 'https://wh.meituan.com/meishi/pn10/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
count=0
#with open(r'D:\python\file\page3.csv','w',newline='')as csvfile:
with open(r'D:\python\file\page10.csv','w',newline='',encoding='utf-8')as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['poiId','title','allCommentNum','avgScore','address','avgPrice'])
    # 发起访问请求
    page = requests.get(url = url, headers = headers)
    # 输出返回信息
    print(page.url)
    print(page.status_code)
    for k,v in page.headers.items():
        print(k,":\t",v)
    # 初始化 soup 对象
    soup = BeautifulSoup(page.text,"html.parser")
    soup = soup.find_all("script")
    #soup = soup.find_all("li")
    for item in soup:
        content=item.get_text()
        for match in re.finditer('"poiId":(.*?),"frontImg":(.*?),"title":"(.*?)","avgScore":(.*?),"allCommentNum":(.*?),"address":"(.*?)","avgPrice":(.*?),',content):
            Info_list=[]
            Info_list.append(match.group(1))
            Info_list.append(match.group(3))
            Info_list.append(match.group(4))
            Info_list.append(match.group(5))
            Info_list.append(match.group(6))
            Info_list.append(match.group(7))
            writer.writerow(Info_list)
            count=count+1
print(count)
print('-----End-----')
