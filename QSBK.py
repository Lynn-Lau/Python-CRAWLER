#-*- coding:utf-8 -*-
"""
Try to fetch the content of QSBK

Author:lynn-lau
Date:2016-05-31
IDE:Pycharm 5.1
Language:Python 2.7
"""
import re
import urllib
import urllib2
import thread
import time

# creat the QSBK class
class QSBK:
    # initiate the theory and define some variates
    def __init__(self):
        self.pageIndex = 1
        # define headers and pretend it is a browser
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
                          '(KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
        self.headers = {'User-Agent':self.user_agent}
        # define stories[] to storage the story
        self.stories = []
        # decide whether continue to store stories into the storage
        self.enable = False

    # define a theory which can fetch the whole code f the web
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            the_page = response.read()
            # decode the web code into utf-8
            pageCode = the_page.decode('utf-8')
            return pageCode

        # try to fetch what's wrong when we can connect to the server
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "There is something wrong when connected to QSBK",e.reason
                return None

    # Using regular to match the content we need and store them into the stories
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "Something wrong when loading the pageCode..."
            return None

        # that 's the regular used to match the content
        pattern = r'<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>' \
                  r'.*?<i.*?number">(.*?)</i>'
        program = re.compile(pattern,re.S)
        # find all content which matched the regular
        items = re.findall(program,pageCode)
        pageStories = []
        for item in items:
            # item[0] is username, item[1] is the story,item[2] is the vote number
            pageStories.append([item[0],item[1],item[2]])
        return pageStories

    # when the first page comes to the end try to fetch the next page
    def loadPage(self):
        # when decided continue to store the stories into the storage
        if self.enable == True:
            # decide the time when continue to store the stories
            if len(self.stories) < 2:
                # if the number of stories less than 2, than we try to fetch the next page's
                # content, match the stories and store them into the storage
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    # page number adds
                    self.pageIndex += 1

    # try to load the story one by one by one
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            # fetch the input from the keyboard
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            #print "OK"
            print "Here comes the story\n",story[0],story[1],story[2]

    # 
    def start(self):
        print "We are loading the stories,press 'Enter' check the new story,press 'Q' quit..."
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()