# Lab-09

```text
UUID Generator を Python で作る

標準ライブラリである uuid  を利用して、Python で UUID を変数に格納して、print するソースコードを書いて、何度か実行してみましょう。

利用するライブラリ/メソッドなど：uuid.uuid4()
```

- Lab-09 では、Python の標準ライブラリである `uuid` を利用して、自作の UUID Generator (簡易版)を作ってみましょう
  - 標準ライブラリは Python の実行環境が整っていれば `import` 句を利用してプログラム内に取り込み、利用することができます

- `uuid` ライブラリについて
  - 公式ドキュメント
    - <https://docs.python.org/ja/3/library/uuid.html#uuid.uuid4>
  - ランダムな UUID を生成するには、`uuid` ライブラリに用意されている `uuid.uuid4()` というメソッドを呼び出すことで実現することができます

- 以下のように、自分の作成するプログラムで uuid ライブラリを取り込みます

```python
# uuid ライブラリを利用するために、取り込む
import uuid

# ライブラリに用意されているメソッドを実行し、その結果を出力する
print(uuid.uuid4())
```

***

- 実行結果(例)
  - 実行するたびに、異なるランダムな UUID が出力されていれば OK です

```bash
(venv) 2021/09/21_04:28:08 Lab-09 % python lab_09.py 
515f7d26-4a84-4641-ba3f-1d210429c5c1

(venv) 2021/09/21_04:28:10 Lab-09 % python lab_09.py 
fe35c12a-fcbd-4b06-b470-54826419acc0

(venv) 2021/09/21_04:28:10 Lab-09 % python lab_09.py 
3872de85-9ed6-4391-b50d-c38d35139aae
```
