# Lab-05

```text
変数 a, b の値を好きな文字列値に変更して calculations.py を作成、実行してみましょう。

（Option）変数 a の文字列を全て大文字/小文字にしてみましょう。
※ print(a.upper()), print(a.lower()) で確認可能
```

- Lab-05 では Python で利用可能なデータ型である `str` 型(文字列型)を扱ってみましょう
  - 文字列に対する操作（フォーマットや書き換えなど）を、str 型データ同士の演算やメソッドを利用することで行うことができます

- 以下のように、演算子を str 型のデータに対して利用することができます

```python
# 文字列のデータを変数に格納する
a = "Hello"
b = "World"

# 変数の中身を出力してみる
print(a)
# 変数の中身を出力してみる(f-string の利用)
print(f"{a}, {b}")

# 文字列のデータに対して演算をしてみる
print(a + b)

# データ型を確認してみる
print(type("hello"))
print(type(a))

# 文字列型データで利用できるメソッドを呼び出してみる
print(a.upper())
```

***

- 実行結果(例)

```bash
# 文字列の結合などの処理を行ってみる
(venv) 2021/09/21_03:45:57 Lab-05 % python lab_05.py 
Hello
World
HelloWorld
Hello, World
HelloHelloHello
False

# 文字列型データに対して利用することができる組み込みのメソッドを使ってみる
(venv) 2021/09/21_03:46:01 Lab-05 % python lab_05_option.py 
HELLO
hello
WORLD
world
```
