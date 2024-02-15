from socket import gethostname, getaddrinfo

# 実行端末のホスト名を取得
HOSTNAME = gethostname()
print(HOSTNAME)

# 実行端末の IP アドレスを取得
LOCAL_IPS = getaddrinfo('localhost', None)
for ip in LOCAL_IPS:
    print(ip[4][0])
