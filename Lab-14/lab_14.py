import os
import shutil


# 1. Touch
with open('hello.txt', 'a'):
    pass

# 2. Check
if os.path.exists('hello.txt'):
    print('hello.txt exists')
else:
    print('File does not exist')
print()

# 3. copy
# use shutil.copy2() if copying with file-metadata
shutil.copy('./hello.txt', './world.txt')

# 4. write
with open('./world.txt', 'a') as f:
    f.write('Hello World from Python')

with open('./world.txt', 'r') as f:
    a = f.read()
print(a)
print()

# 5. rename
os.rename('./world.txt', './hwakabh.txt')
os.system('ls -al')
print()

# 6. Remove
for f in ('./hello.txt', './hwakabh.txt'):
    os.remove(f)
os.system('ls -al')
print()
