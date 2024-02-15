# Lab-24

```text
以下の関数を作成してみましょう

vCenter 管理下にある ESXi ホスト名の一覧を REST-API 経由でリストで取得する関数

vCenter 認証情報:
  FQDN: resvc.haas.local
  IP: 10.111.1.140
  Username: administrator@vsphere.local
  Password: VMware1!

```

- Lab-24 では少し実践的な関数を作成して利用してみましょう

- vSphere REST-API 利用手順の概略
  - Session Token の払い出し
    - `/rest/com/vmware/cis/session` への POST
  - Host 情報に関する REST-API を呼び出し
    - `/rest/vcetner/host` への GET

- vSphere REST-API に関する情報
  - Developer Center
    - <https://VCENTER_FQDN/apiexplorer>
    - vCSA アプライアンス内に含まれている HTML ドキュメントが、Developer Center から確認できる
  - VMware Developer Documentation
    - <https://developer.vmware.com/docs/vsphere-automation/latest/vcenter/>
    - インターネット上にある VMware 提供の公式ドキュメント

***

- 実行結果(例)

```bash
(venv) 2021/09/21_05:50:27 Lab-24 % python lab_24.py 
>>> Fetching session token to call API
>>> Listing up ESXi hosts
esxi05.haas.local
esxi04.haas.local
esxi06.haas.local
sb-esxi02.haas.local
sb-esxi03.haas.local
sb-esxi01.haas.local
10.111.1.165
esxi12.haas.local
esxi11.haas.local
sb-esxi08.haas.local
sb-esxi07.haas.local
sb-esxi09.haas.local
sb-esxi06.haas.local
sb-esxi04.haas.local
sb-esxi05.haas.local
>>> Terminating session
Success
```
