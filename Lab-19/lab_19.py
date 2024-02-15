import paramiko


IP_ADDR = '10.111.1.166'
PORT = 22
USERNAME = 'eyamazaki'
PASSWORD = 'VMware1!'

CMD = 'ip addr'


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    IP_ADDR,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    timeout=5.0
)

stdin, stdout, stderr = client.exec_command(CMD)
# For avoiding Exception in: <function BufferedFile.__del__>
stdin.close()


# stdout を出力
for l in stdout:
    print(l)

client.close()
