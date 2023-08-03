#!/usr/bin/python3
import subprocess

# execute a shell command and get the output
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)

# print the output
print(result.stdout.decode('utf-8'))


# execute a shell command that includes a pipe
result = subprocess.run('ls -l | grep py', shell=True, stdout=subprocess.PIPE)

# print the output
print(result.stdout.decode('utf-8'))

p = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)

# get the output
output, _ = p.communicate()

# print the output
print(output.decode('utf-8'))
