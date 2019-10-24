hostnames = "hosts"
commands = "commandos"

def run_action(host, commands):
    print("Connetion zu {}".format(host))
    print("Kommandoausführung auf remote shell:")
    for c in commands:
        print("Execute {}".format(c))
    print("Connetcion beenden")

with open(hostnames) as fd:
    hosts = fd.readlines()

with open(commands) as fd:
    cmds = fd.readlines()

for host in hosts:
    run_action(host, cmds)
