# update-jenkins

[![CircleCI](https://circleci.com/gh/iganari/update-jenkins/tree/master.svg?style=svg)](https://circleci.com/gh/iganari/update-jenkins/tree/master)

## Shell 版

+ LTS update

```
sh update-jenkins.sh lts
```

+ 任意
    + 数値チェック有り(WIP)

```
sh update-jenkins.sh hogehoge
```

+ 最新Versionを入れる(not LTS)

```
sh update-jenkins.sh latest
```

## Python 版

+ Version

```
# python --version

Python 3.6.2
```

+ 仮想環境について
    + 作成

    ```
    python3 -m venv .update-jenkins
    ```

    + 仮想環境の有効化

    ```
    source .update-jenkins/bin/activate
    ```

    + 必要なライブラリをpip installする

    ```
    pip install -r requirements.txt
    ```

    + 無効化

    ```
    deactivate
    ```

+ [機能] 使用出来るバージョンの確認をする

```
WIP
python3 update-jenkins.py -c
OR
python3 update-jenkins.py --check
```

+ [機能] JenkinsのWARをダウンロードして入れ替える + Jenkinsの再起動
    + LTS版

    ```
    WIP
    python3 update-jenkins.py -v lts
    ```
    
    + 最新版

    ```
    WIP
    python3 update-jenkins.py -v latest
    ```

    + Version指定( :warning: WIP :warning: )

    ```
    WIP
    python3 update-jenkins.py -v 2.153
    ```



## 簡易環境

### docker

+ dockerを用いてスクリプトの簡易動作試験場を作る

```
cd opsfiles/docker
sh dcs.sh status
```

+ コンテナ内ログインしたい場合 ---> :whale:

```
### CentOSコンテナに入る
docker exec -it update-jenkins_centos /bin/bash

### Ubuntuコンテナに入る
docker exec -it update-jenkins_ubuntu /bin/bash
```




+ :warning: :whale: Jenkinsの確認(ダミーファイル)

```
# ls -la /usr/lib/jenkins/jenkins.war 
-rw-r--r-- 1 root root 0 Jan 17 11:14 /usr/lib/jenkins/jenkins.war
```
