# Python


## VS Codeでのメモ


### VS Code上で実行したい

+ すでに `.vscode/tasks.json` がある場合
    + VS Code上で以下のコマンドを実行

```
[Shift] + [Ctrl] + [b] の同時押し
```


+ `.vscode/tasks.json` が無い場合
    + 以下のファイルを作成する

```
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "lts",
            "type": "shell",
            "command": "python3 update-jenkins.py --support lts",
            "group": {
                "kind": "build",
                "isDefault": false
            }
        },
        {
        
            "label": "latest",
            "type": "shell",
            "command": "python3 update-jenkins.py --support latest",
            "group": {
                "kind": "build",
                "isDefault": false
            }
        }
    ]
}
```