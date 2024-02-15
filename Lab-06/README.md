# Lab-06

```text
条件式を任意のものに変更して、if ブロックに流れる条件、else ブロックに流れる if ... else ... 構文を作成してみましょう。
条件式に真になるもの（1 == 1 など）に変更し、else ブロックを省略したロジックを作成してみましょう。
```

- Lab-06 では Python で利用可能なデータ型である `bool` 型(論理値型/Boolean 型)を扱ってみましょう
  - 論理値は `True` と `False` とを値に持つデータで、文字列型の `"True"` と `"False"` とは別物
  - 処理系(Python インタプリタ)の内部では、0 と 1 と同値として扱われます

- bool 型は `if ... else ...` の制御構文(=条件分岐)と密接な関係があります
  - 条件分岐は、条件式が 真(True) なのか 偽(False) なのかという、条件式の評価結果に応じて処理がことなる制御構文であるため

- 以下のように、演算子を bool 型のデータに対して利用することができます

```python
# 論理値型のデータを変数に格納する
a = True
b = False

# 変数の中身を出力してみる
print(f"a is {a}")
# int 型として強制的に出力してみる
print("%i" % a)

# 文字列同士の演算を評価し、その結果に応じて、処理を分岐させる
# この場合、"Hello" と "World" との文字列が等しいか、が条件になり、結果は 偽(False) となるため、print("Not Equal") が出力される
if ("Hello" == "World"):
    print("Equal")
else:
    print("Not Equal")
```

***

- 実行結果(例)

```bash
(venv) 2021/09/21_04:01:42 Lab-06 % python lab_06.py 
a is True
b is False

1
0

True
Not true
Not Equal
```
