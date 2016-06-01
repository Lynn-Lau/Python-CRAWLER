# -*- coding:utf-8 -*-
"""
按照既定的规则抓取楼层的帖子

Author:lynn-lau
Date:2016-06-01
IDE:Pycharm 5.0.4
Language:Python 2.7.10

"""

import urllib
import urllib2
import re

class BDTB:

    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    def getPage(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            the_page = response.read()
            print the_page
            return response

        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print 'There is something wrong with it when connect to the sever',e.reason
                return None
baseURL = 'http://tieba.baidu.com/p/3138733512'
BDTB = BDTB(baseURL,1)
BDTB.getPage(1)