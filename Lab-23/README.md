# Lab-23

```text
以下の関数を作ってみましょう

URL（文字列）を引数に取り、URL の HTML データを取得する関数
引数となる URL には http://abehiroshi.la.coocan.jp （阿部寛 HP の URL）を渡す
戻り値は HTML データ文字列
```

- Lab-23 でも、Lab-22 同様に自作の関数を作成してみましょう
  - Lab-10 で学習した、HTTP GET を行う処理を、Lab-22 で学習した関数の作成と組み合わせて、特定の URL が与えられた場合にそのサイトの HTML データを取得する関数を作ってみましょう

***

- 実行結果(例)

```bash
# requests ライブラリを利用して関数を実装した場合
(venv) 2021/09/21_05:45:22 Lab-23 % python lab_23_requests.py 
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

# urllib ライブラリを利用して関数を実装した場合
(venv) 2021/09/21_05:45:27 Lab-23 % python lab_23_urllib.py 
b'<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">\n<meta name="GENERATOR" content="JustSystems Homepage Builder Version 20.0.6.0 for Windows">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<title>\x88\xa2\x95\x94\x8a\xb0\x82\xcc\x83z\x81[\x83\x80\x83y\x81[\x83W</title>\n</head>\n<frameset cols=18,82>\n  <frame src="menu.htm" marginheight="0" marginwidth="0" scrolling="auto" name="left">\n  <frame src="top.htm" marginheight="0" marginwidth="0" scrolling="auto" name="right">\n  <noframes>\n  <body></body>\n  </noframes>\n</frameset>\n</html>'
```
