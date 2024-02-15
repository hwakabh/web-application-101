# Lab-10

```text
阿部寛の HP に Python でアクセスする

外部ライブラリである requests を pip でインストールして、阿部寛の HP の HTML データを取得してみましょう。
（sandbox 環境の Paiza の方は、外部ライブラリが利用できないので、標準ライブラリの urllib.request を利用してやってみましょう）

利用するライブラリ/メソッドなど：requests.get()
```

- Lab-10 では、ライブラリを用いて、ネットワーク上にあるウェブサーバから HTML データを取得(HTTP GET)してみましょう

- Python で HTTP GET を行うためにはいくつかの方法があります
  - 外部ライブラリである `requests` を利用する
    - `pip` などのパッケージマネージャにより requests ライブラリを実行環境にインストールする必要があります
      - `pip install requests`
    - 公式ドキュメント
      - <https://docs.python-requests.org/en/latest/>
  - 標準ライブラリである `urllib` を利用する
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/urllib.request.html#module-urllib.request>

***

- 実行結果(例)

```bash
# requests ライブラリを利用した場合
(venv) 2021/09/21_04:32:21 Lab-10 % python lab_10_requests.py 
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<meta name="GENERATOR" content="JustSystems Homepage Builder Version 20.0.6.0 for Windows">
<meta http-equiv="Content-Style-Type" content="text/css">
<title>¢°Ìz[y[W</title>
</head>
<frameset cols=18,82>
  <frame src="menu.htm" marginheight="0" marginwidth="0" scrolling="auto" name="left">
  <frame src="top.htm" marginheight="0" marginwidth="0" scrolling="auto" name="right">
  <noframes>
  <body></body>
  </noframes>
</frameset>
</html>

# urllib ライブラリを利用した場合
(venv) 2021/09/21_04:32:28 Lab-10 % python lab_10_urllib.py 
b'<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">\n<meta name="GENERATOR" content="JustSystems Homepage Builder Version 20.0.6.0 for Windows">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<title>\x88\xa2\x95\x94\x8a\xb0\x82\xcc\x83z\x81[\x83\x80\x83y\x81[\x83W</title>\n</head>\n<frameset cols=18,82>\n  <frame src="menu.htm" marginheight="0" marginwidth="0" scrolling="auto" name="left">\n  <frame src="top.htm" marginheight="0" marginwidth="0" scrolling="auto" name="right">\n  <noframes>\n  <body></body>\n  </noframes>\n</frameset>\n</html>'
```
