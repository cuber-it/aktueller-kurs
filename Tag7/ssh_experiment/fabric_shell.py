# noch nicht funktionierend!
from fabric import Connection

# Replace the following with your own host, user, and pass
host = 'localhost:2222'
user = 'paramiko'
password = 'password'

# Create a connection
c = Connection(host=host, user=user, connect_kwargs={"password": password})

# Run a command (this example gets the system's uptime)
result = c.run('uptime')

# Print the result
print("uptime:", result.stdout.strip())
