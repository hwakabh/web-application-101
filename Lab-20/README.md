# Lab-20

```text
ブラウザ操作

Selenium を用いて Google Chrome で https://www.vmware.com/jp.html を開き、ブラウザを閉じる操作を自動化してみましょう。
（※ 要 chromedriver インストール）
```

- Lab-20 では、外部ライブラリを用いて、Python でブラウザ操作を自動化してみましょう

- ライブラリのインストール(pip の場合)
  - `pip install selenium`
  - 公式ドキュメント
    - <https://www.selenium.dev/documentation/>

- Chromedriver の設定
  - ダウンロード先
    - <https://chromedriver.chromium.org/downloads>

***

- 実行結果(例)

```bash
# chromdriver がインストールされており、パスが通っていることを確認する
(venv) 2021/09/21_05:30:49 Lab-20 % which chromedriver
/usr/local/bin/chromedriver

# プログラムの実行
(venv) 2021/09/21_05:30:55 Lab-20 % python lab_20.py 
#---> ブラウザが自動的に起動し、プログラム中で指定した URL へアクセスされる

# ブラウザによる HTML のレンダリングが終了すると、自動的にウィンドウが閉じられる
(venv) 2021/09/21_05:31:14 Lab-20 % 
```
