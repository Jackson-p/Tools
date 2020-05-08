# -*- coding:utf-8 -*-

'''
爬取某个用户的所有issue主要是适合保存备份, 注意一次最多只能请求30条数据，所以要先拿到页数，
然后再分页请求
'''

import re
import time
import pip._vendor.requests as requests

print('输入github用户名')
user_name = input()


page_url = "https://api.github.com/search/issues?q=+state:open+repo:" + user_name + "/" + user_name + ".github.io"
page_res = requests.get(page_url)
page_header = str(page_res.headers)
page_rels = re.findall(r'page=(\d+)', page_header)
page_number = int(page_rels[1])




def getIssues(page):
    url = "https://api.github.com/search/issues?q=+state:open+repo:" + user_name + "/" + user_name + ".github.io&sort=created&page=" + str(page)
    issues = requests.get(url).json().get('items')
    for issue in issues:
        title = issue['title']
        label = (issue['labels'] and issue['labels'][0]['name']) + '~~'  # be careful diffrom js
        body = issue['body']
        name = label + title + '.md'
        with open(name, 'a') as f:
            f.write(body)
        print(title + "写入完毕")
    time.sleep(10)


for x in range(page_number):
    print('爬取第' + str(x+1) + '页中...')
    getIssues(x+1)