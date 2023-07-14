from netmiko import ConnectHandler

def run(device, cmd, type, verbose=False):
    results = {}
    commands = [ cmd ]
    if type == 'batch':
        with open(cmd) as fd:
            commands = [line for line in fd.read().splitlines() if not line.startswith("#")]
    connection = None
    try:
        connection = ConnectHandler(**device)
        for cmd in commands:
            output = connection.send_command(cmd)
            results[cmd] = output
            if verbose:
                print(f"Command: {cmd}\n{output}\n")
    finally:
        if connection:
            connection.disconnect()
    return results
