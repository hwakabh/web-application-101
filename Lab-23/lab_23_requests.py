import requests


def get_html_contents(site_url: str) -> str:
    resp = requests.get(url=site_url)
    return resp.text


ABE_HIROSHI_URL = 'http://abehiroshi.la.coocan.jp'

html = get_html_contents(site_url=ABE_HIROSHI_URL)
print(html)
