#!/usr/bin/env python
# cording: utf-8

### Doc
# https://jenkins.io/changelog-stable/

import sys


args = sys.argv

if len(args) == 1:
    print("引数がありません")
elif len(args) == 2:
    print(args[1])
elif len(args) > 2:
    print("引数が多すぎます")


import feedparser

RSS_URL = 'https://jenkins.io/changelog-stable/rss.xml'

jenkins_lts_dic = feedparser.parse(RSS_URL)

# print (jenkins_lts_dic.feed.title)
# print (jenkins_lts_dic.feed.title_detail)
# print (jenkins_lts_dic.feed.updated)
# print (jenkins_lts_dic.feed.item[0].title)
# print (jenkins_lts_dic.feed)
# print (jenkins_lts_dic)
print (jenkins_lts_dic.entries[0].title, jenkins_lts_dic.entries[0].link)
print (jenkins_lts_dic.entries[0].link)

lts_link = jenkins_lts_dic.entries[0].link
print(lts_link)

lts_ver = lts_link.split("#") 
print (lts_ver)
print (lts_ver[1])

