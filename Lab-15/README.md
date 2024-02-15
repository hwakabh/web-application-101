# Lab-15

```text
さまざまなデータ形式のファイルを扱う（CSV / JSON）

以下の2ファイルを作成して、それぞれ Python で読み込み、”VMware” のみを出力させてみましょう
Amazon, Google, Microsoft, Oracle, IBM, Hewlett Packard, VMware の文字列が並んだ CSV ファイル
Amazon, Google, Microsoft, VMware のティッカーシンボルと会社名とを記載した JSON ファイル

利用するライブラリ/メソッド：open(), with, csv.reader() / open(), json.load()
```

- Lab-15 では、CSV や JSON などのデータ型のファイルやその中のデータを扱ってみましょう
  - Lab-14 で行ったファイル操作に加えて、データ形式に合わせてライブラリを利用してみましょう
  - `csv.reader()`
    - CSV 形式のファイルの読み込み
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/csv.html?highlight=csv.reader#csv.reader>
  - `json.load()`
    - JSON 形式のファイルの読み込み
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/json.html?highlight=json.load#json.load>

***

- 実行結果(例)

```bash
# CSV 形式のファイルを読み込んで、特定データを出力
(venv) 2021/09/21_05:01:01 Lab-15 % python lab_15_csv.py 
VMware

# JSON 形式のファイルを読み込んで、特定データを出力
(venv) 2021/09/21_05:01:06 Lab-15 % python lab_15_json.py 
VMware
```
