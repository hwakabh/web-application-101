# Lab-19

```text
SSH アクセス

Paramiko を用いて Linux サーバにアクセスしてみましょう
```

- Lab-19 では、外部ライブラリを用いて、Python で SSH を利用し、リモートサーバ上でコマンドを実行してみましょう

- ライブラリのインストール(pip の場合)
  - `pip install paramiko`
  - 公式ドキュメント
    - <http://docs.paramiko.org/en/stable/>

***

- 実行結果(例)
  - リモートサーバ上で、`ip addr` コマンドを実行した場合

```bash
(venv) 2021/09/21_05:25:49 Lab-19 % python lab_19.py 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000

    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

    inet 127.0.0.1/8 scope host lo

       valid_lft forever preferred_lft forever

    inet6 ::1/128 scope host 

       valid_lft forever preferred_lft forever

2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000

    link/ether 00:50:56:b8:75:60 brd ff:ff:ff:ff:ff:ff

    inet 10.111.1.166/25 brd 10.111.1.255 scope global ens160

       valid_lft forever preferred_lft forever

    inet6 fe80::250:56ff:feb8:7560/64 scope link 

       valid_lft forever preferred_lft forever
```
