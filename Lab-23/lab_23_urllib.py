import urllib.request


def get_html_contents(site_url: str) -> str:
    req = urllib.request.Request(url=site_url)
    with urllib.request.urlopen(req) as res:
        html = res.read()
        #-> byte 文字列で戻る

    return str(html)


ABE_HIROSHI_URL = "http://abehiroshi.la.coocan.jp/"

res = get_html_contents(site_url=ABE_HIROSHI_URL)
print(res)
