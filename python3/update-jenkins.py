#!/usr/bin/env python
# cording: utf-8

### Long-term Support (LTS) 
# https://jenkins.io/changelog-stable/rss.xml

### Weekly
# https://jenkins.io/changelog/rss.xml


import sys
import os

def parse_opts():

    # from argparse import ArgumentParser
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--support',
        '-s',
        required=True,
        dest='support',
        help='Usage: python3 ' + __file__ + ' {lts|latest}'
    )

    return parser.parse_args()

def check_args(args):

    if args.support == 'lts' or args.support == 'latest':
        # pass
        print('ok')
    else:
        print('Support Argument is {lts|latest}')
        sys.exit(1)


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
            # print('OK')
            pass
        else:
            print ( jks_war_file + 'がシンボリックリンクでは無いため、プログラムを継続出来ません')
            sys.exit(0)
    else:
        print("PATHが間違っているか、そもそもインストールされてない可能性があります")
        sys.exit(1)

def get_jks_war():
    import shutil
    import requests

    jks_war_dir  = '/usr/lib/jenkins'
    jks_war_file = jks_war_dir + '/jenkins.war'
    
    # jks_war_dir_new = jks_war_dir + '/' + chk_jks_ver()
    # jks_war_file_new = jks_war_dir + '/' + chk_jks_ver() + '/jenkins.war'
    jks_war_file_new_link = 'http://updates.jenkins-ci.org/download/war/' + chk_jks_ver() + '/jenkins.war'

    if os.path.isfile(jks_war_dir + '/' + chk_jks_ver() + '/jenkins.war'):
        print ('既に本体ファイルがあります')
        # sys.exit(0)
    elif os.path.isdir(jks_war_dir + '/' + chk_jks_ver()):
        print ('予期していないディレクトリがありましたので終了します')
        sys.exit(0)
    else:
        # versionに合わせて、ディレクトリを作成する
        os.mkdir(jks_war_dir + '/' + chk_jks_ver())

        # version毎のディレクトリの下にJenkinsの本体warをダウンロードする
        res = requests.get(jks_war_file_new_link,stream=True)
        with open(jks_war_dir + '/' + chk_jks_ver() + '/jenkins.war', "wb") as fp:
            shutil.copyfileobj(res.raw,fp)

def chg_jks_symbolic():

    jks_war_dir  = '/usr/lib/jenkins'
    
    jks_war_file = jks_war_dir + '/jenkins.war'

    os.unlink(jks_war_file)
    os.symlink(jks_war_dir + '/' + chk_jks_ver() + '/jenkins.war', jks_war_file)
    

def restart_jks():
    os.system('systemctl stop   jenkins')
    os.system('systemctl start  jenkins')
    os.system('systemctl status jenkins')


# main
def main(args):
 
    # 引数のチェック
    # chk_args() <----- OLD
    check_args(args)
    # print ('引数 = ' + args[1] + ' の文字数に問題はありません')




    # # 引数を元に参照すべきURLを決定する
    # print('今回、ダウンロードすべきURL = ' + rss_url())
    # # dw_url = rss_url()
    # # print('今回、ダウンロードすべきURL = ' + dw_url)

    # # 引数で要求されたJenkinsのバージョンを取る
    # # jks_ver = chk_jks_ver()
    # # print (jks_ver)
    # print ('今回、ダウンロードしたいJenkinsのバージョン = ' + chk_jks_ver())

    # # jenkinsの本体jarについてのチェックを行う
    # chk_war_file()

    # # 任意のVersionのjenkinsをダウンロードする
    # get_jks_war()

    # # シンボリックリンクの付け替えを行う
    # chg_jks_symbolic()
    # # sys.exit(0)

    # # Jenkinsのプロセスの再起動を行う
    # restart_jks()


if __name__ == '__main__':

    args = parse_opts()

    main(args)
