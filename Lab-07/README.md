# Lab-07

```text
“VMW” を key として指定して “VMware” を取り出すのではなく、”Google” を取り出すように変更してみましょう。
存在しない key（例えば “DELL” など）を指定して出力の違いを確認してみましょう。
存在しない key:value ペアを追加してみましょう。
サンプルを参考にディクショナリ型の持つメソッドを実行してみて出力を確認してみましょう。
```

- Lab-07 では Python で利用可能なデータ型である `dict` 型(辞書型/Dictionary 型)を扱ってみましょう
  - dict 型のデータは、Key と Value との組み合わせで複数のデータを一つの変数に束ねて格納することができます

- 以下のように、dict 型のデータに対して、データを格納して、値を参照することができます

```python
# dict 型のデータを定義、出力する
companies = {
    "VMW": "VMware",
    "GOOG": "Google",
    "AAPL": "Apple",
    "AMZN": "Amazon",
    "MSFT": "Microsoft"
}
print(companies)


# Key を指定して、Value を取り出す
print(companies.get('VMW'))

# dict 型のデータ型で利用可能なメソッドを呼び出す
print(companies.keys())
```

***

- 実行結果(例)

```bash
(venv) 2021/09/21_04:10:24 Lab-07 % python lab_07.py 
{'VMW': 'VMware', 'GOOG': 'Google', 'AAPL': 'Apple', 'AMZN': 'Amazon', 'MSFT': 'Microsoft'}

Google
Google

{'VMW': 'VMware', 'GOOG': 'Google', 'AAPL': 'Apple', 'AMZN': 'Amazon', 'MSFT': 'Microsoft', 'DELL': 'Dell Technologies'}

dict_keys(['VMW', 'GOOG', 'AAPL', 'AMZN', 'MSFT', 'DELL'])
dict_values(['VMware', 'Google', 'Apple', 'Amazon', 'Microsoft', 'Dell Technologies'])
dict_items([('VMW', 'VMware'), ('GOOG', 'Google'), ('AAPL', 'Apple'), ('AMZN', 'Amazon'), ('MSFT', 'Microsoft'), ('DELL', 'Dell Technologies')])
```
