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

+ 仮想環境の有効化

```
source .update-jenkins/bin/activate
```

+ 必要なライブラリをpip installする

```
pip install -r requirements.txt
```

+ 使用出来るバージョンの確認をする

```
WIP
python3 update-jenkins.py -c
OR
python3 update-jenkins.py --check
```

+ JenkinsのWARをダウンロードして入れ替える + Jenkinsの再起動
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


+ 仮想環境の無効化

```
deactivate
```

## 簡易環境

### docker

+ :whale: dockerを用いてスクリプトの簡易動作試験場を作る

```
cd opsfiles/docker
sh docker-build-run.sh
```

