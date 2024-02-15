# Lab-11

```text
ホスト名や IP アドレスの取得

Bash や PowerShell では hostname や ifconfig（ip addr）コマンドと似たようなことを Python でやってみましょう
利用するライブラリ/メソッドなど：socket.gethostname(), socket.getaddrinfo()
```

- Lab-11 では、`socket` ライブラリを用いて、実行環境のネットワーク情報を確認してみましょう
  - `socket.gethostname()`
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/socket.html#socket.gethostname>
  - `socket.getaddrinfo()`
    - 公式ドキュメント
      - <https://docs.python.org/ja/3/library/socket.html#socket.getaddrinfo>

***

- 実行結果(例)

```bash
# シェルから確認
(venv) 2021/09/21_04:46:43 Lab-11 % hostname
hwakabh-mac

(venv) 2021/09/21_04:46:47 Lab-11 % ifconfig lo0
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
  options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
  inet 127.0.0.1 netmask 0xff000000 
  inet6 ::1 prefixlen 128 
  inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
  nd6 options=201<PERFORMNUD,DAD>

# Python から確認
(venv) 2021/09/21_04:46:52 Lab-11 % python lab_11.py 
hwakabh-mac
127.0.0.1
127.0.0.1
::1
::1
```
