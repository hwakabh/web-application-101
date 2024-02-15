# Lab-18

```text
QR コード生成

qrcode[pil] を用いて https://www.vmware.com/jp.html へのリンクを持つ QR コードを生成、画像ファイル(.png 形式)に保存してアクセスしてみましょう
```

- Lab-18 では、外部ライブラリを用いて、Python で QR コードを生成してみましょう

- ライブラリのインストール(pip の場合)
  - `pip install qrcode[pil]`
  - 公式ドキュメント
    - <https://github.com/lincolnloop/python-qrcode>

***

- 実行結果(例)
  - プログラム中で指定したファイル名で、QR コードが記載された画像ファイルが生成され、カメラなどで読み込んだ時に目的のサイトに遷移できれば OK です

```bash
(venv) 2021/09/21_05:21:41 Lab-18 % ls -al 
total 16
-rw-r--r--   1 hwakabh  staff   756 Sep 21 05:21 README.md
drwxr-xr-x   4 hwakabh  staff   128 Sep 21 02:39 .
drwxr-xr-x  33 hwakabh  staff  1056 Sep 16 17:01 ..
-rw-r--r--   1 hwakabh  staff   135 Sep 15 18:40 lab_18.py

# プログラムで QR コードを生成
(venv) 2021/09/21_05:21:43 Lab-18 % python lab_18.py 

# ファイルが作成されているのを確認
(venv) 2021/09/21_05:21:46 Lab-18 % ls -al
total 24
-rw-r--r--   1 hwakabh  staff   699 Sep 21 05:21 vmware_jp.png
drwxr-xr-x   5 hwakabh  staff   160 Sep 21 05:21 .
-rw-r--r--   1 hwakabh  staff   756 Sep 21 05:21 README.md
drwxr-xr-x  33 hwakabh  staff  1056 Sep 16 17:01 ..
-rw-r--r--   1 hwakabh  staff   135 Sep 15 18:40 lab_18.py

# QR コードを確認してみる
(venv) 2021/09/21_05:21:48 Lab-18 % open vmware_jp.png 
```
