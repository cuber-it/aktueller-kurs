import asyncio
import asyncssh

async def run_client(host, command):
    async with asyncssh.connect(host) as conn:
        result = await conn.run(command)
        print(result.stdout, end='')

async def run_multiple_clients(hosts, command):
    tasks = (run_client(host, command) for host in hosts)
    await asyncio.gather(*tasks)

hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3']  # Replace with your hosts
command = 'ls'  # Replace with your command

# Run the asyncio event loop
asyncio.run(run_multiple_clients(hosts, command))
