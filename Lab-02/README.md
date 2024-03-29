# Lab-02

```text
Lab-1 の print(“Hello World”) を変数を利用して出力してみましょう
変数の中身を好きな文字列に変えてみましょう
```

- Lab-02 では、"Hello World" という文字列データを変数に格納して、使ってみましょう
  - Python に限らず、プログラミング言語において、`変数` は処理したいデータを格納しておくものになります
  - 今回のようなシンプルな場合には必ずしも利用する必要はないですが、一般に何かの処理をする際には、変数にデータを格納します

- Python では、`変数名 = データ` の形で、変数にデータを格納することができます
  - 変数名は開発者が自由に命名して問題ありませんが、利用できないものがあったり、ある程度のガイドラインにならって命名します
    - PEP8 と呼ばれる規約に記載があります
      - <https://www.python.org/dev/peps/pep-0008/#naming-conventions>
  - `a = "hello"` という場合、変数 `a` に `"hello"` という文字列のデータを格納することになります

***

- 実行結果(例)

```bash
# ファイルを作り、プログラムを実行してみる
(venv) 2021/09/21_03:27:33 Lab-02 % python lab_02.py 
Hello world

# エディタを開いて、変数に格納するデータである "Hello World" を変更してみる

# 変更後に再度プログラムを実行してみる
(venv) 2021/09/21_03:27:45 Lab-02 % python lab_02.py 
Hello VMware PSO
```
