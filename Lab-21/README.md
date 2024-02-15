# Lab-21

```text
Twitter クライアント

Tweepy を用いて VMware のツイート（@VMware）を取得してみましょう
（※ 要 Twitter Developer 登録）
```

- Lab-21 では、外部ライブラリを用いて、Twitter API を呼び出てみましょう
  - VMware 公式 Twitter アカウント
    - <https://twitter.com/vmware>

- ライブラリのインストール(pip の場合)
  - `pip install tweepy`
  - 公式ドキュメント
    - <https://docs.tweepy.org/en/stable/>

- Twitter Developer 登録の参考手順
  - <https://qiita.com/newt0/items/66cb76b1c8016e9d0339>

***

- 実行結果(例)

```bash
# Developer 登録をして得られた認証キーを環境変数に設定する
# (取得した Twitter アカウントに紐づくものなので、自身のものに置き換えてください)
(venv) 2021/09/21_05:54:49 Lab-21 % export CUSTOMER_KEY='xxxxxxxxxxxxxxxxxxxx'
(venv) 2021/09/21_05:54:59 Lab-21 % export CUSTOMER_SECRET='yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
(venv) 2021/09/21_05:55:01 Lab-21 % export ACCESS_TOKEN='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
(venv) 2021/09/21_05:55:04 Lab-21 % export ACCESS_SECRET='vvvvvvvvvvvvvvvvvvv'

# 直近のツイート5個を取得する
(venv) 2021/09/21_05:55:06 Lab-21 % python lab_21.py 
----------
2021-09-20 19:16:06
VMware 💙 Kubernetes 

Learn how to extend #Kubernetes to public clouds and edge environments at #VMworld 2021. Register now for 100% free &amp; online access → https://t.co/hgvDqqZnKj https://t.co/YtHTP5GAOb
----------
2021-09-20 18:44:31
RT @narayan___b: Warming up for @VMworld with new #VMWonAWS features..
1) 2-Host i3en clusters
2) Storage only scale-out warnings
3) Host r…
----------
2021-09-20 16:36:40
RT @vmwarenews: We’re thrilled to be joining a collective of 200+ signatories focused on actionable change. The time for climate action is…
----------
2021-09-20 16:05:11
Reach the cloud 46% faster with 59% less staff time. It’s possible with #VMware Cloud on #AWS. Learn more from a new @IDC study. 
https://t.co/ebsjtcV25Z https://t.co/asBABfEowy
----------
2021-09-20 15:22:13
RT @CormacJHogan: TKG v1.4 – Some nice new features https://t.co/93uOkpnVoX
```
