import urllib.request


target_url = "http://abehiroshi.la.coocan.jp/"

req = urllib.request.Request(url=target_url)

# with を使う場合
with urllib.request.urlopen(req) as res:
    html = res.read()

print(html)
#-> byte 文字列で戻る
