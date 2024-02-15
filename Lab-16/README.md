# Lab-16

```text
YAML を扱う

Amazon, Google, Microsoft, VMware の企業概要をまとめた YAML を作成し、PyYAML を用いて読み込み、VMware に関する情報を出力してみましょう。
```

- Lab-16 では、外部ライブラリの `PyYAML` を利用して、YAML ファイルに記載されたデータを扱ってみましょう
  - サンプル YAML ファイル（例）:
    - <https://gitlab.eng.vmware.com/psoj-red-office-hours/web-application-development/-/blob/master/Lab-16/companies.yaml>

- ライブラリのインストール(pip の例)
  - `pip install PyYAML`
  - 公式ドキュメント
    - <https://pyyaml.org>
    - PyYAML では、YAML ファイル内のデータを読み込み、dict 型として扱うことができる

***

- 実行結果(例)

```bash
# YAML データのうち、VMware に関するもののみを取り出し
(venv) 2021/09/21_05:13:54 Lab-16 % python lab_16.py 
{'name': 'vmware', 'tickerSymbol': 'VMW', 'foundYear': 1998, 'founderName': 'Diane Greene', 'isGafa': False}
```
