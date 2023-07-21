import sys
print(sys.argv)

import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument for the command
parser.add_argument("command", help="the command to be executed")

# Add an optional argument for the -h option
parser.add_argument("-f", help="the help string for the command")

# Add an argument for the filename
parser.add_argument("filename", help="the filename to be processed")

# Add an argument for the '--' option
parser.add_argument("--", dest="other_stuff", help="an option for the command", nargs='*')

# Parse the arguments
args = parser.parse_args()

# Now you can access the arguments as properties of the args object
print(args.command)
print(args.h)
print(args.filename)
print(args.__)
