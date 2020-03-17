import argparse

# create an instance of ArgumentParser without any arguments
parser = argparse.ArgumentParser()

# use the add_argument method to specify a positional argument called filename and
# provide some help text using the help argument.
parser.add_argument('filename', help='the file to read')

# tell the parser to parse the arguments from stdin using the parse_args method and
# store the parsed arguments as to the variable args
args = parser.parse_args()
print(args)