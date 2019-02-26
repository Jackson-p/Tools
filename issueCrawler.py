# -*- coding:utf-8 -*-

'''
爬取某个用户的所有issue主要是适合保存备份
'''


import urllib.request as urll
import json
import re
import time

print('输入github用户名')
user_name = input()


center_url = "https://api.github.com/search/issues?q=+state:open+repo:" + user_name + "/" + user_name + ".github.io"
response = urll.urlopen(center_url)
header = str(response.headers)
rels = re.findall(r'page=(\d+)',header)
page_number = int(rels[1])

def getIssues(page):
    url = "https://api.github.com/search/issues?q=+state:open+repo:" + user_name + "/" + user_name + ".github.io&sort=created&page=" + str(page)
    issues = urll.urlopen(url).read().decode('utf-8')
    issues = json.loads(issues)['items']
    for issue in issues:
        title = issue['title']
        label = issue['labels'][0]['name'] + '~~'  # be careful diffrom js
        body = issue['body']
        name = label + title + '.md'
        with open(name, 'a') as f:
            f.write(body)
        print(title + "写入完毕")
    time.sleep(10)

for x in range(page_number):
    print('爬取第' + str(x) + '页中')
    getIssues(x+1)