#!/usr/bin/env python
# cording: utf-8

### Long-term Support (LTS) 
# https://jenkins.io/changelog-stable/rss.xml

### Weekly
# https://jenkins.io/changelog/rss.xml


import sys
import os

def rss_url():
    if args[1] == 'lts':
        rss_url = 'https://jenkins.io/changelog-stable/rss.xml'
    elif args[1] == 'latest':
        rss_url = 'https://jenkins.io/changelog/rss.xml'
    else:
        print('引数が不正です')
        sys.exit(1)
    return rss_url

def chk_jenkins_ver():
    import feedparser

    url = rss_url()
    jenkins_dic = feedparser.parse(url)
    
    full_version = jenkins_dic.entries[0].link
    only_version = full_version.split("#v")[1]
    #  print(only_version)
    return only_version


def chk_war_file():
    # import datetime
    # import shutil

    jenkins_war_dir  = '/usr/lib/jenkins'
    jenkins_war_file = jenkins_war_dir + '/jenkins.war'

    if os.path.isfile(jenkins_war_file):
        if os.path.islink(jenkins_war_file):
            print('OK')
        else:
            print ('must create link')
            # print(jenkins_war_dir + '/' + jenkins_ver)
            # os.mkdir(jenkins_war_dir + '/' + jenkins_ver)
            # os.mkdir(jenkins_war_dir + '/backup_' + datetime.datetime.today().strftime("%Y%m%d"))
    else:
        print("PATHが間違っているか、そもそもインストールされてない可能性があります")
        sys.exit(1)

def get_jenkins_war():
    import shutil
    import requests


    jenkins_war_dir  = '/usr/lib/jenkins'
    jenkins_war_file = jenkins_war_dir + '/jenkins.war'
    jenkins_war_dir_new = jenkins_war_dir + '/' + chk_jenkins_ver()
    jenkins_war_file_new = jenkins_war_dir + '/' + chk_jenkins_ver() + '/jenkins.war'
    jenkins_war_file_new_new_link = 'http://updates.jenkins-ci.org/download/war/' + chk_jenkins_ver() + '/jenkins.war'


    os.mkdir(jenkins_war_dir_new)

    res = requests.get(jenkins_war_file_new_new_link,stream=True)
    with open(jenkins_war_file_new, "wb") as fp:
        shutil.copyfileobj(res.raw,fp)

def chg_jenkins_symbolic():
    print("WIP")

def restart_jenkins():
    print("WIP")








if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print("引数を入れてください")
        sys.exit(1)
    elif len(args) == 2:
        print(args[1])

        jenkins_ver = chk_jenkins_ver()
        print(jenkins_ver)

        RSS_URL = rss_url()
        print(RSS_URL)

        chk_war_file()

        # 任意のVersionのjenkinsをダウンロードする
        get_jenkins_war()

        # シンボリックリンクの付け替えを行う
        chg_jenkins_symbolic()

        # Jenkinsのプロセスの再起動を行う
        restart_jenkins()

    elif len(args) > 2:
        print("引数が多すぎます")
        sys.exit(1)
    # print(RSS_URL)
    

    
    # jenkins_ver = jenkins_ver()
    # print(jenkins_ver)
