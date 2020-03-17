import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')

# add a --limit flag
# - to specify that an argument is a flag, we need to place two hyphens at the beginning the flag’s name.
# - we specified a shorter version of the flag as our second argument
# - we used the type option for add_argument to state that we want the value converted to an integer
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')

args = parser.parse_args()
print(args)