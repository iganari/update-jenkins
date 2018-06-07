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




# print("hogehoge")
