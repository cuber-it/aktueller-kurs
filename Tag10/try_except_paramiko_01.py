import paramiko

def remote_execute(hostname, username, password, command):
    # Create a new SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    ssh.connect(hostname, username=username, password=password)

    while True:
        try:
            # Execute a command
            stdin, stdout, stderr = ssh.exec_command(command)

            # Read from stdout and stderr
            stdout_content = stdout.read()
            stderr_content = stderr.read()

            # If there's content in stderr, it usually means an error occurred.
            if stderr_content:
                raise Exception(f"An error occurred during command execution: {stderr_content.decode()}")

            # Print the output
            print('STDOUT:')
            print(stdout_content.decode())
        finally:
            print(f"Dinge die immer zu tun sind, evtl. auch bei Abbruch")

    # Close the connection
    ssh.close()

# Call the function with your specific details
remote_execute('hostname', 'username', 'password', 'command')
