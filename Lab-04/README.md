# Lab-04

```text
変数 a, b の値を好きな整数値に変更して calculations.py を作成、実行してみましょう。

（Option）計算結果をそれぞれ変数に格納してデータ型を確認してみましょう。
※ print(type(変数名)) で確認可能
```

- Lab-04 では Python で利用可能なデータ型である `int` 型(整数値型)を扱ってみましょう
  - Python で利用可能な算術演算は以下の通りです
    - 加算(+)
    - 減算(-)
    - 乗算(*)
    - 冪算(**)
    - 除算(/)
    - 除算: 浮動小数点以下の切り捨て(//)
    - 剰余算(%)

- 以下のように、算術演算子を int 型のデータに対して利用することができます
  - `print()` の `f-string (フォーマット済み文字列リテラル)` を利用することで、`print()` の引数に変数を指定して、変数の内容を自動展開することができます
    - <https://docs.python.org/ja/3.9/tutorial/inputoutput.html>

```python
# 整数値のデータをそれぞれ変数に代入する
a = 12
b = 4

# 変数の中身を出力してみる(f-string の利用)
print(f"a is {a}")

# 計算結果を出力してみる
print(a + b)

# データ型を確認してみる
print(type(12))
print(type(a))
```

***

- 実行結果(例)

```bash
# 計算結果の出力
(venv) 2021/09/21_03:42:48 Lab-04 % python lab_04.py 
a is 12
b is 4

Add
16
Subtract
8
Multiply 1
48
Multiply 2
20736
Divide 1
3.0
Divide 2
3
Divide 3: Surplus
0

# Optional: 計算結果を格納する変数のデータ型を出力
(venv) 2021/09/21_03:43:00 Lab-04 % python lab_04_option.py 
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'float'>
<class 'int'>
<class 'int'>
```
