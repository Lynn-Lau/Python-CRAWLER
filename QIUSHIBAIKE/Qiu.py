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

# Using 'use_agent' and 'headers' to pretend it is a Browser
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
headers = {'User-Agent':user_agent}

url ='http://www.qiushibaike.com/'

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    the_page = response.read()
    # print the_page
    # remind you that you have Successfully got them
    print "Congratulations! You have already fetched the whole content of the Web!!!"

    content = the_page.decode('utf-8')

    # Make a rule
    pattern = r'<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>' \
              r'.*?<i.*?number">(.*?)</i>'
    program = re.compile(pattern,re.S)
    items = re.findall(program,content)
    for item in items:
        # item[0] is user name，item[1] is the content，item[2] is the votes
        print item[0],item[1],item[2]

    #Tell me why if there is some thing wrong with it
except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
else:
    pass



