pythonによるOSC通信テンプレ

新しい環境の作成
$ cd [project dir]
$ python3 -m venv [newenvname]
venv という名前でプロジェクトディレクトリ直下に作成しておく（$ python3 -m venv venv）のが良い．ディレクトリ移動 → venv アクティベート → 作業 という流れができたり，IDE によっては 1 つのプロジェクト内でソースコードと一緒に venv も管理できるので．

Activate
Linux，Mac
$ . [newenvname]/bin/activate
Windows
$ .\[newenvname]\Scripts\activate

Deactivate
([newenvname])$ deactivate

受信 -> osc.py
送信 -> python_color_hex-def/index.py