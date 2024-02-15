# Lab-01

```text
”Hello World” という文字列を出力するプログラムを書いてみましょう
次に、”Hello VMware PSO” など好きな文字列に変更してみましょう
```

- Lab-01 では Python で "Hello World" をしてみましょう
  - 新しいプログラミング言語をまず動かしてみる場合には、慣例として "Hello World" という文字列をコンソールに表示することから始めるケースが多いです
  - 技術的には、実行環境の OS の stdout を Python から呼び出すことを試すということになります

- Python では、特定の文字列をコンソールに出力するには、`print()` というメソッドを利用します

***

- sandbox 環境（Paiza）を利用する方向け
  - <https://paiza.io/ja/projects/new> にアクセスして、プログラムを書いてみましょう

- 既に手元に Python 環境がインストールされている方向け
  - `hello.py` など好きな名前で Python のプログラムを作成して、実行してみましょう。

***

- 実行結果(例)

```bash
# ファイルを作ってみてプログラムを実行する
(venv) 2021/09/21_03:19:03 Lab-01 % python lab_01.py 
hello

# エディタを開いて "hello" の文字列を変更してみる

# 変更後に再度プログラムを実行してみる
(venv) 2021/09/21_03:19:17 Lab-01 % python lab_01.py 
Hello World
```
