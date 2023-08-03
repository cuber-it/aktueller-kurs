#!/usr/bin/python3
import asyncio

async def main():

    # execute a shell command and get the output
    proc = await asyncio.create_subprocess_exec('ls', '-l', stdout=asyncio.subprocess.PIPE)
    stdout, _ = await proc.communicate()
    print(stdout.decode())

    # execute a shell command that includes a pipe
    proc = await asyncio.create_subprocess_shell('ls -l | grep py', stdout=asyncio.subprocess.PIPE)
    stdout, _ = await proc.communicate()
    print(stdout.decode())

    # execute a shell command and get the output
    proc = await asyncio.create_subprocess_exec('ls', '-l', stdout=asyncio.subprocess.PIPE)
    stdout, _ = await proc.communicate()
    print(stdout.decode())

# Python 3.7+
asyncio.run(main())
