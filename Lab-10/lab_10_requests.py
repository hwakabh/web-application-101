import requests

target_url = "http://abehiroshi.la.coocan.jp/"

resp = requests.get(target_url)
print(resp.text)
