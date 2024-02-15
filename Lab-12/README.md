# Lab-12

```text
外部コマンドの呼び出し

シェル側で追加した外部のコマンド（例えば kubectl など）を Python から呼び出して実行し、その結果をみてみましょう
PATH が通っている必要あり、そうでない場合には、フルパスを引数に指定
利用するライブラリ/メソッドなど： os.system(), subprocess.call(), subprocess.Popen()
```

- Lab-12 では、実行環境にインストールされている外部コマンドを Python から呼び出してみましょう
  - `os.system()`
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/os.html#os.system>
  - `subprocess.call()`
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/subprocess.html#subprocess.call>
  - `subprocess.Popen`
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/subprocess.html#subprocess.Popen>

***

- 実行結果(例)
  - `subprocess.Popen` を利用して、kind (Kubernetes in Docker) コマンド `kind version` を呼び出す場合

```bash
# シェルから呼び出す場合
(venv) 2021/09/21_04:42:42 Lab-12 % kind version
kind v0.8.1 go1.14.2 darwin/amd64

# Python から呼び出す場合
(venv) 2021/09/21_04:42:44 Lab-12 % python lab_12.py 
0
b'kind v0.8.1 go1.14.2 darwin/amd64\n'
b''
```
