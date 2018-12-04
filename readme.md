# update-jenkins

## 使い方

### shell

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

### Python

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

+ JenkinsのWARをダウンロードする
    + LTS版

    ```
    python3 update-jenkins.py lts
    ```
    
    + 最新版

    ```
    python3 update-jenkins.py latest
    ```

    + Version指定( :warning: WIP :warning: )

    ```
    python3 update-jenkins.py 2.153
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

