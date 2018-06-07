#!/usr/bin/env python
# cording: utf-8

### Doc
# https://jenkins.io/changelog-stable/

import sys
# import ElementTree
from xml.etree import ElementTree as ET
# import urllib
# from urllib.request import urlopen
from urllib import urlopen
# import urlopen

args = sys.argv

if len(args) == 1:
    print("引数がありません")
elif len(args) == 2:
    print(args[1])
elif len(args) > 2:
    print("引数が多すぎます")


# rssを読み込む

url = 'https://jenkins.io/changelog-stable/rss.xml'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    XmlData = response.read()

# 読み込んだrssを解析する

root = ET.fromtring(XmlData)

# print("hogehoge")

print(root.tag,root.attrid)

