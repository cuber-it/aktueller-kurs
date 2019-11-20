import base64
import paramiko

key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))

client = paramiko.SSHClient()

client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)
try:
    client.connect('ssh.example.com', username='strongbad', password='thecheat')

    stdin, stdout, stderr = client.exec_command('ls')

    for line in stdout:
        print('... ' + line.strip('\n'))
finally:
    client.close()
