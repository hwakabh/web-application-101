# Lab-17

```text
Excel（CSV）操作

Padas または openpyxl を用いて田町オフィスのロッカーレイアウト（Locker.xlsx）をダウンロード + Python で読み込んで、自分の名前を出力してみましょう。
```

- Lab-17 では、外部ライブラリを用いて、Python で Excel ファイル内のデータを扱ってみましょう
  - 田町ロッカーレイアウト
    - <https://onevmw.sharepoint.com/:x:/r/teams/PSOJapanEmployeeOnly/Shared%20Documents/General/Office%20Guide/Tamachi%20Office/Locker.xlsx?d=w90c8ca3400994d9bbaee9101e6c68d0a&csf=1&web=1&e=IeQedi>
  - ダウンロード済みのもの
    - <https://gitlab.eng.vmware.com/psoj-red-office-hours/web-application-development/-/blob/master/Lab-17/Locker.xlsx>

- ライブラリのインストール(pip の例)
  - `openpyxl` を利用する場合
    - `pip intall openpyxl`
    - 公式ドキュメント
      - <https://openpyxl.readthedocs.io/en/stable/>
  - `pandas` を利用する場合
    - `pip intall pandas`
    - 公式ドキュメント
      - <https://pandas.pydata.org>

***

- 実行結果(例)
  - `openpyxl` を利用した場合

```bash
# Excel ファイル内のシート一覧と特定セル内のデータを出力
(venv) 2021/09/21_05:17:41 Lab-17 % python lab_17.py 
['Locker Place', '16F\u3000Locker', '17F Locker', '18F Locker']
若林　寛之
```
