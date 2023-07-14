import paramiko

# Create a new SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
ssh.connect(hostname='localhost', port=2222, username='paramiko', password='password')

# Execute a command
stdin, stdout, stderr = ssh.exec_command('ls -l')

# Print the output of the command
for line in stdout:
    print(line.strip('\n'))

# Close the connection
ssh.close()
