# Python のプログラムの中で環境変数を取得して確認したり、設定（追加・上書き）、削除したりするには os.environ を使う。
# なお、環境変数の設定や削除による変更はその Python プログラムの中でのみ有効。システムの環境変数が書き換わるわけではない。

import os

# # os.environ を利用するケース
# envs = os.environ
# print(envs)
# print(envs['SHELL'])

# os.getenv() を利用するケース
envs = os.getenv('SHELL')
# envs = os.getenv('MY_ENV', None)
print(envs)