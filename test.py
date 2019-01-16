# -*- coding:utf-8 -*-

'''
爬取某个用户的所有issue主要是适合保存备份
'''


import urllib.request as urll
import json

print('输入github用户名')
user_name = input()
print('0 提取所有issue，1 提取自己的issue')
choice = input()


response = urll.urlopen("https://api.github.com/repos/" + user_name + "/" + user_name + ".github.io/issues").read().decode('utf-8')
response = json.loads(response) # get dict type


for issue in response:
    user = issue['user']['login']
    title = issue['title']
    label = issue['labels'][0]['name'] + '~~' # be careful diffrom js
    body = issue['body']
    name = label + title + '.md'
    if choice == 1 and user != user_name:
        continue
    with open(name, 'a') as f:
        f.write(body)
    print(title + "写入完毕")
