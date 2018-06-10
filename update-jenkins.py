#!/usr/bin/env python
# cording: utf-8

### Long-term Support (LTS) 
# https://jenkins.io/changelog-stable/rss.xml

### Weekly
# https://jenkins.io/changelog/rss.xml


# jenkins => jks


import sys
import os


def chk_args():
    # args = sys.argv
    if len(args) == 1:
        print ('引数をいれてください')
        sys.exit(0)
    elif len(args) == 2:
        # print ('OK')
        pass 
    elif len(args) > 2:
        print ('引数が多すぎます')
        sys.exit(0)

def rss_url():
    if args[1] == 'lts':
        rss_url = 'https://jenkins.io/changelog-stable/rss.xml'
    elif args[1] == 'latest':
        rss_url = 'https://jenkins.io/changelog/rss.xml'
    else:
        print('引数が不正です')
        sys.exit(1)
    return rss_url

def chk_jks_ver():
    import feedparser

    url = rss_url()
    jks_dic = feedparser.parse(url)
    
    full_version = jks_dic.entries[0].link
    only_version = full_version.split("#v")[1]
    #  print(only_version)
    return only_version


def chk_war_file():
    # import datetime
    # import shutil

    jks_war_dir  = '/usr/lib/jenkins'
    jks_war_file = jks_war_dir + '/jenkins.war'

    if os.path.isfile(jks_war_file):
        if os.path.islink(jks_war_file):
            print('OK')
        else:
            print ('準備が出来ていません')
            sys.exit(0)
    else:
        print("PATHが間違っているか、そもそもインストールされてない可能性があります")
        sys.exit(1)

def get_jks_war():
    import shutil
    import requests


    jks_war_dir  = '/usr/lib/jenkins'
    jks_war_file = jks_war_dir + '/jenkins.war'
    jks_war_dir_new = jks_war_dir + '/' + chk_jks_ver()
    jks_war_file_new = jks_war_dir + '/' + chk_jks_ver() + '/jenkins.war'
    jks_war_file_new_new_link = 'http://updates.jenkins-ci.org/download/war/' + chk_jks_ver() + '/jenkins.war'


    os.mkdir(jks_war_dir_new)

    res = requests.get(jks_war_file_new_new_link,stream=True)
    with open(jks_war_file_new, "wb") as fp:
        shutil.copyfileobj(res.raw,fp)

def chg_jks_symbolic():

    jks_war_dir  = '/usr/lib/jenkins'
    jks_war_file = jks_war_dir + '/jenkins.war'

    # os.


    print("WIP")
    

def restart_jks():
    print("WIP")








if __name__ == '__main__':
 
    # 引数のチェック
    args = sys.argv
    chk_args()
    print ('引数 = 'args[1] + 'に問題は無い　')

    # 引数で要求されたJenkinsのバージョンを取る
    jks_ver = chk_jks_ver()
    print(jks_ver)

    RSS_URL = rss_url()
    print(RSS_URL)

    chk_war_file()

    # 任意のVersionのjenkinsをダウンロードする
    get_jks_war()

    # シンボリックリンクの付け替えを行う
    chg_jks_symbolic()

    # Jenkinsのプロセスの再起動を行う
    restart_jks()


    # print(RSS_URL)
    

    
    # jenkins_ver = jenkins_ver()
    # print(jenkins_ver)