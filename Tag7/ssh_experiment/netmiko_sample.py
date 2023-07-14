from netmiko import ConnectHandler

device = {
   'device_type': 'linux',
   'ip':   '127.0.0.1',
   'username': 'paramiko',
   'password': 'password',
   'port' : 2222,          # optional, default 22
   #'secret': 'secret',  # optional, default ''
   'verbose': True,     # optional, default False
}

connection = ConnectHandler(**device)

output = connection.send_command('ls -l /')
print(output)

connection.disconnect()
