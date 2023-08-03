#!/usr/bin/python3
import os

# Create a child process
# os.fork() returns 0 in the child process and child's pid in the parent process
pid = os.fork()
# Nach dem fork in Beiden!
if pid > 0: # der Elternteil
    # This is the parent process
    # pid contains the child process id
    print('I am parent process:')
    print('Process ID:', os.getpid())
    print('Child\'s process ID:', pid)
else : # Der Kindteil
    # This is the child process
    print('\nI am child process:')
    print('Process ID:', os.getpid())
    print('Parent\'s process ID:', os.getppid())

    print('Calling an external program in child process')
    os.execlp("/bin/bash", "bash", "-c", "ls -l")
