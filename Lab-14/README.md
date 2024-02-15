# Lab-14

```text
ファイル操作

以下の一連のファイル操作を Python でやってみましょう

1. 空ファイル hello.txt の作成
2. 1 で作成したファイルが存在するか確認
3. 1 で作成した hello.txt を world.txt として別名でコピー
4. 3 で作成した world.txt に好きな文字列（”Hello from Python” など）を書き込み、中身を確認
5. 3 で作成した world.txt を好きなファイル名にリネームして、確認
6. 両方のファイルを削除、確認

利用するライブラリ/メソッド：open(), os.path.exists(), with, write(), read(), shutil.copy(), os.rename(), os.remove()
```

- Lab-14 では一般的なファイル操作を Python から行ってみましょう
  - `open()`
    - ファイルを開く
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/functions.html?highlight=open#open>
  - `read()`
    - ファイルの中身を Python が扱える形で読み出す
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/io.html?highlight=write#io.TextIOBase.read>
  - `write()`
    - ファイルに対して、Python からデータを書き込む
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/io.html?highlight=write#io.TextIOBase.write>
  - `os.path.exists()`
    - ファイルの存在確認
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/os.path.html?highlight=os.path.exists#os.path.exists>
  - `os.rename()`
    - ファイルのリネーム
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/os.html?highlight=os.rename#os.rename>
  - `os.remove()`
    - ファイル削除
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/os.html?highlight=os.remove#os.remove>
  - `shutil.copy()`
    - ファイルのコピー
      - タイムスタンプなどのメタデータはコピーされないため、`shutil.copy2()` を利用するケースもある
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/shutil.html?highlight=shutil.copy#shutil.copy>

***

- 実行結果(例)
  - 一連の流れを通しで行う(最終的に作成したファイルはクリーンナップされる)場合
  - それぞれの挙動確認のために、部分的にコメントアウトなどをして確認してみましょう

```bash
(venv) 2021/09/21_04:56:42 Lab-14 % python lab_14.py 
hello.txt exists

Hello World from Python

total 24
drwxr-xr-x   6 hwakabh  staff   192 Sep 21 04:56 .
drwxr-xr-x  33 hwakabh  staff  1056 Sep 16 17:01 ..
-rw-r--r--   1 hwakabh  staff  2192 Sep 21 04:56 README.md
-rw-r--r--   1 hwakabh  staff     0 Sep 21 04:56 hello.txt
-rw-r--r--   1 hwakabh  staff    23 Sep 21 04:56 hwakabh.txt
-rw-r--r--   1 hwakabh  staff   642 Sep 15 17:54 lab_14.py

total 16
drwxr-xr-x   4 hwakabh  staff   128 Sep 21 04:56 .
drwxr-xr-x  33 hwakabh  staff  1056 Sep 16 17:01 ..
-rw-r--r--   1 hwakabh  staff  2192 Sep 21 04:56 README.md
-rw-r--r--   1 hwakabh  staff   642 Sep 15 17:54 lab_14.py
```
