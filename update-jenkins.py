#!/usr/bin/env python
# cording: utf-8

### Long-term Support (LTS) 
# https://jenkins.io/changelog-stable/
# https://jenkins.io/changelog-stable/rss.xml

### Weekly
# https://jenkins.io/changelog/
# https://jenkins.io/changelog/rss.xml

import sys

def rss_url():
    if args[1] == 'lts':
        rss_url = 'https://jenkins.io/changelog-stable/rss.xml'
    elif args[1] == 'latest':
        rss_url = 'https://jenkins.io/changelog/rss.xml'
    else:
        print('引数が不正です')
        sys.exit(1)
    return rss_url

def chk_war_file():
    import os
    jenkins_war_dir  = '/usr/lib/jenkins'
    jenkins_war_file = jenkins_war_dir + '/jenkins.war'

    if os.path.isfile(jenkins_war_file):
        if os.path.islink(jenkins_war_file):
            print('OK')
        else:
            print ('must create link')
    else:
        print("must create")


if __name__ == '__main__':
    
    args = sys.argv
    
    if len(args) == 1:
        print("引数を入れてください")
        sys.exit(1)
    elif len(args) == 2:
        print(args[1])
        # if args[1] == 'lts':
        #     RSS_URL = 'https://jenkins.io/changelog-stable/rss.xml'
        # elif args[1] == 'latest':
        #     RSS_URL = 'https://jenkins.io/changelog/rss.xml'
        # else:
        #     print('引数が不正です')
        #     sys.exit(1)
        RSS_URL = rss_url()
    elif len(args) > 2:
        print("引数が多すぎます")
        sys.exit(1)

    print(RSS_URL)
    
    import feedparser
    
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

    chk_war_file()

# def test():
#     comment = "iganari test"
#     return comment
# 
# if __name__ == '__main__':
#     s = test()
#     print(s)
