#-*- coding:utf-8 -*-
"""
Try to fetch Qiushibaike content

Author:lynn-lau
IDE:Pycharm 5.0
Language:Python 2.7
Date:2016-05-30
"""
import re
import urllib
import urllib2

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
headers = {'User-Agent':user_agent}
url ='http://www.qiushibaike.com/'
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    the_page = response.read()
    # print the_page
    print "Congratulations! You have already fetched the whole content of the Web!!!"
    content = the_page.decode('utf-8')
    pattern = r'<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>' \
              r'.*?<i.*?number">(.*?)</i>'
    program = re.compile(pattern,re.S)
    items = re.findall(program,content)
    for item in items:
        # item[0]为用户名，item[1]为段子的内容，item[2]获得的赞数
        print item[0],item[1],item[2]
    #print items
except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
#else:


