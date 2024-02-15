import os
import subprocess
from sys import stderr

CMD = 'kind version'
# # suppressing output
# CMD = 'kind version >/dev/null 2>&1'

# # 1. os.system() を利用するケース, ret は type: int となる
# ret = os.system(CMD)
# print(ret)

# # 2. subprocess.call() を利用するケース, ret は type: int となる
# ret = subprocess.call(CMD, shell=True)
# print(ret)

# 3. subprocess.Popen を利用するケース
ret = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = ret.communicate()
print(ret.returncode)
print(stdout)
print(stderr)
