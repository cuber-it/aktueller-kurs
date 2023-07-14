
import argparse
import sys
import cmdrunner


def args():
    parser = argparse.ArgumentParser(description="SSH connection parameters")
    parser.add_argument('--device_type', default='linux', help='Device type for Netmiko')
    parser.add_argument('--ip', default='127.0.0.1', help='IP address of the device')
    parser.add_argument('username', help='Username for SSH connection')
    parser.add_argument('password', help='Password for SSH connection')
    parser.add_argument('--port', type=int, default=22, help='SSH port (default: 22)')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument("command", help='Command to be executed')
    parser.add_argument("--type", default='single', help="Batchfile")


    return parser.parse_args()


if __name__ == "__main__":
    args = args()
    device = {
       'device_type': args.device_type,
       'ip':   args.ip,
       'username': args.username,
       'password': args.password,
       'port' : args.port,
       'verbose': args.verbose,
    }
    try:
        print("Verarbeitung startet ...")
        result = cmdrunner.run(device, cmd=args.command, type=args.type, verbose=args.verbose)
        print("Verarbeitung abgeschlossen")
        if args.verbose:
            print(result)
        exit(0)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)
